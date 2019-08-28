#Python3
#source env/bin/activate
import requests, time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://pisa.ucsc.edu/class_search/index.php')
#Make sure we're on the correct site
assert 'UC Santa Cruz - Schedule of Classes' in browser.title

# elem = browser.find_element_by_name('select')
# elem.send_keys('seleniumhq' + Keys.RETURN)

#Keep term at Fall 2019 for now
# term_dropdown = browser.find_element_by_id('term_dropdown')
#For status, click on all classes instead of open classes
all_classes = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[4]/div/select/option[2]')
all_classes.click()

search = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[15]/div/input')
search.click()

# html = browser.page_source
# print(html)
#open link in new tab
# class_link.send_keys(Keys.COMMAND + 'enter')
# class_link.send_keys(Keys.CONTROL + 't')
# windows = browser.window_handles
# time.sleep(3)
# driver.switch_to.window(windows[1])

def handle_class(class_page):
    #gather/store info, click on back button
    print('yay!!!')
    back_button = browser.find_element_by_xpath('//*[@id="back_link"]')
    back_button.click()

# We need to click into every class, grab the information needed, store it in
# the json file, then click back to results. Then continue to the next class
# until at the end of the page then click "next"

# classes = browser.find_element_by_xpath("//*[contains(@id,'class_id_')]")
classes = browser.find_elements_by_css_selector('[id*="class_id_"]')

classes[0].click()
handle_class(classes[0])

# for class_link in classes:
#     time.sleep(3)       #be kind to server
#     class_link.click()
    # handle_class(class_link)




#next_page = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/a')
# time.sleep(3)
# next_page.click()

# browser.quit()
