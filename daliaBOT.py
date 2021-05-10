from selenium import webdriver
import sys
import time
from message_updater import message
import PySimpleGUI as sg

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
# options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', options=options)

sg.theme('Green')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Press start after making sure that WHATSAPP WEB is CONNECTED')],
          [sg.Button('START'), sg.Button('STOP')]]

# Create the Window
window = sg.Window('WAF-BOT', layout)
driver.get('https://web.whatsapp.com/')
# Event Loop to process "events" and get the "values" of the inputs
mes_utils = message(driver, font_group='Repasse - Tipster Régis',
                    forward_group='Repasse BETIPS')

while True:
    event, values = window.read()
    if event == 'START':
        while(1):
            mes_utils.get_last_message()

            if event == sg.WIN_CLOSED or event == 'STOP':  # if user closes window or clicks cancel
                driver.close()
                window.close()
                break
    break
