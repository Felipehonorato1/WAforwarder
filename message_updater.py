from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# <span dir="auto" title="GRUPO A" class="_35k-1 _1adfa _3-8er">GRUPO A</span>
# <span dir="auto" title="GRUPO A" class="_35k-1 _1adfa _3-8er">GRUPO A</span>


class message:
    def __init__(self, driver, font_group, forward_group):
        self.forward_group = forward_group
        self.font_group = font_group
        self.last_message_sent = None
        self.driver = driver
        pass

    def send_message(self, message):

        groupB = self.driver.find_element_by_xpath(
            f"//span[@title='{self.forward_group}']")

        groupB.click()
        print(f'Last message: {message}')

        # <div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div>

        textbox = self.driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        textbox.send_keys(message)

        enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        enviar.click()

        print(f"mensagem enviada as {datetime.now()}")
        self.last_message_sent = message

    def get_last_message(self):
        time.sleep(1)
        groupA = self.driver.find_elements_by_xpath(
            f"//span[@title='{self.font_group}']")

        for element in groupA:
            try:
                element.click()
            except:
                print('Next')

        msg_got = self.driver.find_elements_by_css_selector(
            "span.selectable-text.copyable-text")

        msgs = [message.text for message in msg_got]
        self.check_update(msgs[-1])

    def check_update(self, last_message):
        if last_message != self.last_message_sent:
            self.send_message(last_message)
