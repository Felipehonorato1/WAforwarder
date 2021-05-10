from selenium import webdriver
import sys
import time
from message_updater import message

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
# options.add_argument('--headless')
driver = webdriver.Chrome(
    '/home/felipe/Área de Trabalho/PROJECTS/BOTDalia/chromedriver', options=options)
driver.get('https://web.whatsapp.com/')


mes_utils = message(driver)

input("Press ENTER when connected: ")
# GETTING MESSAGE
while(1):
    mes_utils.get_last_message()
