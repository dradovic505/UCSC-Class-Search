#Python3
#source env/bin/activate
import math, requests, time, mysql.connector
from selenium import webdriver
import yaml

#database set up in class_database.py, now we can use it here
my_credentials = yaml.safe_load(open('db.yaml'))
mydb = mysql.connector.connect(
    host=my_credentials['mysql_host'],
    user=my_credentials['mysql_user'],
    password=my_credentials['mysql_password'],
    database=my_credentials['mysql_db']
)
db = mydb.cursor(prepared=True)

#I'm using firefox
browser = webdriver.Firefox()
browser.get('https://pisa.ucsc.edu/class_search/index.php')

########Functions#########

#Keep term at Fall 2019 for now
# term_dropdown = browser.find_element_by_id('term_dropdown')
#For status, click on all classes instead of open classes
def handle_initial_page():
    all_classes = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[4]/div/select/option[2]')
    all_classes.click()
    search = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[15]/div/input')
    time.sleep(3)
    search.click()
    show_100 = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div/select/option[4]')
    show_100.click()
    time.sleep(3)

def handle_class():
    #get all info needed from page
    subject = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/h2').text
    class_number = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[1]/dl/dd[3]').text
    career = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[1]/dl/dd[1]').text
    status = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[2]/dl/dd[1]').text
    available_seats = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[2]/dl/dd[2]').text
    wait_list_total = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[2]/dl/dd[6]').text
    ge = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[1]/dl/dd[6]').text
    credits = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[1]/dl/dd[5]').text

    #some classes don't have meeting times, room, instructor set
    table_results = browser.find_elements_by_tag_name('td')
    meeting_times = 'N/A'
    room = 'N/A'
    instructor = 'N/A'
    if len(table_results) > 0:
        try:
            meeting_times = table_results[0].text
            room = table_results[1].text
            instructor = table_results[2].text
        except NoSuchElementException:
            print('NoSuchElementException for ' + subject)

    #just return the number of credits, not the ' units' after it
    index = credits.find(' units')
    credits = credits[0:index]

    #place val in database
    query = 'INSERT INTO classes (subject, class_number, career, status,       \
            available_seats, wait_list_total, ge, credits, meeting_times, room,\
            instructor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    vals = (subject, int(class_number), career, status, int(available_seats),   \
           int(wait_list_total), ge, int(credits), meeting_times, room, instructor,)
    db.execute(query, vals)
    mydb.commit()

def handle_page():
    pg_len = len(browser.find_elements_by_css_selector('[id*="class_id_"]'))
    print('pg len: ' + str(pg_len))
    for i in range(pg_len):
        list_classes = browser.find_elements_by_css_selector('[id*="class_id_"]')
        print('pg len internal: ' + str(len(list_classes)))
        time.sleep(2)       #be kind to server
        print('index: ' + str(i))
        list_classes[i].click()
        handle_class()

        #go back to main page
        back_button = browser.find_element_by_xpath('//*[@id="back_link"]')
        time.sleep(2)
        back_button.click()

########End functions########

handle_initial_page()
total_classes = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/b[3]').text
num_pages = math.floor(int(total_classes)/100)
for i in range(num_pages):
    handle_page()
    next_page = browser.find_element_by_link_text('next')
    next_page.click()
browser.quit()
