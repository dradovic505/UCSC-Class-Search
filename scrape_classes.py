#Python3
#source env/bin/activate
import requests, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
# browser.get('https://pisa.ucsc.edu/class_search/index.php')
browser.get('http://codepad.org/')
#Make sure we're on the correct site
# assert 'UC Santa Cruz - Schedule of Classes' in browser.title

# html = browser.page_source
# print(html)

button = browser.find_element_by_xpath('/html/body/div[1]/center/table/tbody/tr/td[1]/div/form/table/tbody/tr[2]/td[1]/nobr[10]/label/input')
button.click()

# elem = browser.find_element_by_name('select')
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()
