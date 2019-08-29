#Python3
#source env/bin/activate
import requests, time, mysql.connector
from selenium import webdriver

#database set up in class_database.py, now we can use it here
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='class_search'
)
db = mydb.cursor()

browser = webdriver.Firefox()
browser.get('https://pisa.ucsc.edu/class_search/index.php')

#Keep term at Fall 2019 for now
# term_dropdown = browser.find_element_by_id('term_dropdown')
#For status, click on all classes instead of open classes
all_classes = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[4]/div/select/option[2]')
all_classes.click()
search = browser.find_element_by_xpath('/html/body/div/form/div/div[2]/div[15]/div/input')
search.click()


subject_names = [
                   'AM', 'ANTH', 'APLX', 'ARBC', 'ART', 'ARTG', 'ASTR', 'BIOC',
                   'BIOE', 'BIOL', 'BME', 'CHEM', 'CHIN', 'CLNI', 'CLTE', 'CMMU',
                   'CMPM', 'COWL', 'CRES', 'CRSN', 'CRWN', 'CSE', 'CSP', 'DANM',
                   'EART', 'ECE', 'ECON', 'EDUC', 'ENVS', 'ESCI', 'FILM', 'FMST',
                   'FREN', 'GAME', 'GERM', 'GRAD', 'GREE', 'HAVC', 'HEBR', 'HIS',
                   'HISC', 'ITAL', 'JAPN', 'KRSG', 'LAAD', 'LALS', 'LATN', 'LGST',
                   'LING', 'LIT', 'MATH', 'MERR', 'METX', 'MUSC', 'OAKS', 'OCEA',
                   'PBS', 'PERS', 'PHIL', 'PHYE', 'PHYS', 'POLI', 'PORT', 'PRTR',
                   'PSYC', 'RUSS', 'SCIC', 'SOCD', 'SOCY', 'SPAN', 'SPHS', 'STAT',
                   'STEV', 'THEA', 'UCDC', 'WRIT'
                ]



def handle_class(class_page):
    #get all info from page, store in val
    /html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/div[2]/dl/dd[6]
    


    #place val in database
    query = 'INSERT INTO classes (subject, class_number, career, status,  \
            available_seats, wait_list_total, ge, credits, meeting_times, \
            room, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, \
            %s, %s)'
    db.execute(query, val)
    mydb.commit()

    #go back to main page
    back_button = browser.find_element_by_xpath('//*[@id="back_link"]')
    back_button.click()


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

# with open('classes.json', 'w') as f:
#         json.dump(class_list, f, indent=2)

# browser.quit()
