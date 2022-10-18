import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
#inicail document consists of Name of Gallery, Address, and Link to the google maps
def window_open():
    driver.get(row[7])  #opening the webpage from the csv file
    driver.implicitly_wait(3)

def emailsearch():
    webbox_link.click() #going to the actual gallery webpage
    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(3)

    page_source = driver.page_source
    url = driver.current_url #getting current url for recording it in case we need it
    EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
    # using regex to find emails on the source page
    list_of_emails = []
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        list_of_emails.append(re_match.group())
    s=[row[0], row[6], url,  list_of_emails]
    print(s)


def check_exists_by_xpath(xpath):
    #for some reason google has different XPaths for the link,
    # so when opening the google maps the link to the website might have different XPath
    # For that reason I added try, except to prevent crashing program each time
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


with open('/Users/kirillevseev/Downloads/google_galleries.csv', newline='') as csvfile:
    list_of_galleries = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(list_of_galleries, None) #skipping the header


    c=0
    for row in list_of_galleries:
        c+=1
        print(c, " ", row[0])
        PATH = '/Users/kirillevseev/Downloads/chromedriver'
        driver = webdriver.Chrome(PATH)
        window_open()

        if check_exists_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a/div[1]/div[2]/div[1]'):
            webbox_link=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a/div[1]/div[2]/div[1]')
            emailsearch()

        elif check_exists_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[15]/div[5]/a/div[1]/div[2]/div[1]'):
            webbox_link = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[15]/div[5]/a/div[1]/div[2]/div[1]')
            emailsearch()
        elif check_exists_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/a/div[1]/div[2]/div[1]'):
            webbox_link = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/a/div[1]/div[2]/div[1]')
            emailsearch()
        driver.quit()


