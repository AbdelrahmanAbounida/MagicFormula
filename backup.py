from main import Magic

username = "" # enter your username
password = "" # enter your password
stocks = 50
market_cap = 230

# here is a proxy of Brazil
proxy = '179.127.241.199:53653'
a = Magic(username,password,stocks,market_cap,proxy)

# this is a sample website that I scrape some data from but now it is supposed that the browser is of Brazil Proxy not Germany

a.login()
a.fill_input()
a.get_stocks()
data = a.get_data()
a.get_sheet(data)





























'''
from urllib.request import urlopen
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open("https://www.magicformulainvesting.com/Account/LogOn")

br.select_form(nr=0)
response = br.response().read()
print(response)

br.form['Email'] = 'abdelrahmanaboneda@gmail.com'
br.form['Password'] = 'Aa2964079.'

br.submit()


print(br.re )


print(response)
soup = BeautifulSoup(response)
print(soup.findAll('td',attrs={'class':'empformbody'}))


  for form in br.forms():
    print("Form name:", form.name)
    print(form)
'''
