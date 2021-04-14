# NOT FINISHED

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

# if len(sys.arv) < 3:
#   raise Exception("Type in address e-mail and a string of text that will be sent.")

my_login = "bomgobango@gmail.com"
my_pass = "dududede4455"

# target_email = sys.argv[1]
# message = sys.argv[2:]

browser = webdriver.Chrome()
browser.get('https://mail.google.com/')
login_field = browser.find_element_by_id('identifierId')
login_field.send_keys(my_login, Keys.ENTER)
time.sleep(2)
browser.refresh()
time.sleep(1)
login_button = browser.find_element_by_link_text('Zaloguj się')
login_button.click()
time.sleep(3.5)
# login_field = browser.find_element_by_class_name('rFrNMe N3Hzgf jjwyfe QBQrY zKHdkd sdJrJc Tyc9J u3bW4e')
# login_field.send_keys(my_login, Keys.ENTER)
# page.send_keys(Keys.ENTER)

time.sleep(120)