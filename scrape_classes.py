#Python3
#source env/bin/activate
import requests, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://pisa.ucsc.edu/class_search/index.php')
#Make sure we're on the correct site
assert 'UC Santa Cruz - Schedule of Classes' in browser.title

# elem = browser.find_element_by_name('select')
# elem.send_keys('seleniumhq' + Keys.RETURN)

#Keep term at Fall 2019 for now
term_dropdown = browser.find_element_by_id('term_dropdown')
#For status, click on all classes instead of open classes
all_classes = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[4]/div/select/option[2]')
all_classes.click()

search = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[15]/div/input')
search.click()

# html = browser.page_source
# print(html)

#Now we have all classes listed. Click "Display first" to show 100 results.
    #We need to click into every class, grab the information needed, store it in
    #the json file, then click back to results. Then continue to the next class
    #until at the end of the page then click "next"


# browser.quit()
