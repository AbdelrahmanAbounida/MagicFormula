import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

webdriverPath = "C:\Program Files (x86)\chromedriver.exe"
link = "https://www.magicformulainvesting.com/"


#browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)

class Magic(webdriver.Chrome):

    def __init__(self, username, password, stocks, market_cap,proxy='179.127.241.199:53653',
                 webdriver_path="C:\Program Files (x86)\chromedriver.exe"):
        self.webdriver_path = webdriverPath
        self.email = username
        self.password = password
        self.stocks = stocks
        self.market_cap = market_cap
        options = Options()
        options.add_argument(f'proxy server={proxy}')
        super(Magic, self).__init__(webdriver_path, chrome_options=options)
        self.implicitly_wait(5)

    def login(self):
        self.get(link)
        login = self.find_element(By.XPATH, '//*[@id="blogin"]/li[2]/a')
        login.click()

        email = self.find_element(By.XPATH, '//input[@id="Email"]')
        password = self.find_element(By.XPATH, '//input[@id="Password"]')
        login = self.find_element(By.XPATH, '//input[@id="login"]')

        email.send_keys(self.email)
        password.send_keys(self.password)
        login.click()

    def fill_input(self):
        market_cap = self.find_element(By.XPATH, '//input[@class="value_display"]')
        market_cap.clear()
        market_cap.send_keys(self.market_cap)

        stocks_choices = self.find_elements(By.XPATH, '//td/span/input')
        choice_30 = stocks_choices[0]
        choice_50 = stocks_choices[1]
        if self.stocks == 30:
            choice_30.click()
        elif self.stocks == 50:
            choice_50.click()
        else:
            print("your choice is wrong")
            self.quit()

    def get_stocks(self):
        get_stocks_button = self.find_element(By.XPATH, '//div[@class="button_left"]/input')
        get_stocks_button.click()


    def get_data(self):
        out = []
        table_headers = self.find_elements(By.XPATH, '//thead/tr/th/h2')
        heads = [x.text for x in table_headers]
        out.append(heads)

        rows = self.find_elements(By.XPATH,'//tbody/tr[@class="altrow"]')
        for i in range(1,len(rows)+1):
            row = self.find_elements(By.XPATH,f'//table[@class="divheight screeningdata"]/tbody/tr[{i}]/td')
            data = [x.text for x in row]
            out.append(data)
            print(data)

        return out


    def get_sheet(self,data):
        with open('out.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)


