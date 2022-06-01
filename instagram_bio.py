# Creation Date: 01/06/2022

import os
import pytz  
import calendar
from time import sleep
from random import randint
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup():
    ''' Returns: Browser session. '''
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(1)
    return browser


def get_secrets():
    ''' Returns: Username and password loaded from ENV. '''
    load_dotenv()
    return os.getenv("USER"), os.getenv("PASS")


def login(browser):
    ''' Purpose: Logs into Instagram via Selenium. '''
    username, password = get_secrets()
    browser.get('https://www.instagram.com/')
    sleep(randint(10,20))
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(randint(10,20))


def build_text():
    ''' Returns: Built Instagram biography string. '''
    current_time = datetime.now(pytz.timezone('Australia/Queensland'))
    hour = current_time.strftime("%I %p").replace(" ", "").lower()
    day = calendar.day_name[current_time.weekday()]
    return f"Feels like {hour} on a {day} to me..."


def update_bio(browser):
    ''' Purpose: Updated Instagram biography as specified. '''
    browser.get('https://www.instagram.com/accounts/edit/')
    sleep(randint(10,20))
    biography_input = browser.find_element_by_css_selector("textarea[id='pepBio']")
    current_text = biography_input.get_attribute("value")
    while True:
        new_text = build_text()
        if current_text != new_text:
            biography_input.clear()
            biography_input.send_keys(new_text)
            update_button = browser.find_element_by_xpath("//*[contains(text(), 'Submit')]")
            update_button.click()
            current_text = new_text
        sleep(randint(30,45))


if __name__ == "__main__":
    while True:
        try:
            browser = setup()
            login(browser)
            update_bio(browser)
        except Exception:
            sleep(randint(1200,1300))