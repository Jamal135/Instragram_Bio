''' Creation Date: 01/06/2022 '''

# External Imports
import os
import sys
import pytz
import calendar
from time import sleep
from random import randint
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta, date
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Internal Imports
from logger_formats import Log

# See selenium locally: http://localhost:4444/ui#/sessions

def setup(method: str = 'local'):
    ''' Returns: Browser session. '''
    options = webdriver.ChromeOptions()
    if method == 'production': 
        browser = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=options
        )
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(5)
    return browser

class EnvironmentError(Exception):
    pass

def get_secrets():
    ''' Returns: Username and password loaded from ENV. '''
    load_dotenv()
    try:
        user = os.environ['USER']
        password = os.environ['PASS']
    except KeyError as e:
        raise EnvironmentError(f'.env {e} not set')
    return user, password

def login(browser: webdriver.Chrome):
    ''' Purpose: Logs into Instagram via Selenium. '''
    username, password = get_secrets()
    browser.get('https://www.instagram.com/')
    sleep(randint(10, 20))
    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(randint(40, 60))

def get_account_details(browser: webdriver.Chrome):
    ''' Purpose: Loads the Instagram accounts page. '''
    browser.get('https://www.instagram.com/accounts/edit/')

def build_text():
    ''' Returns: Built Instagram biography string. '''
    current_time = datetime.now(pytz.timezone('Australia/Queensland'))
    hour = current_time.strftime('%I %p').replace(' ', '').lower().lstrip('0')
    day = calendar.day_name[current_time.weekday()]
    return f'Tell Simon it feels like {hour} on a {day}...'

def get_current(browser: webdriver.Chrome):
    ''' Returns: Current Instagram biography text. '''
    get_account_details(browser)
    sleep(randint(10, 20))
    biography_input = browser.find_element(By.CSS_SELECTOR, "textarea[id='pepBio']")
    return biography_input.get_attribute('value')

def calculate_end(session_days: int = 9):
    ''' Returns: Session restart date. '''
    return date.today() + timedelta(days=session_days)

def verify_update(browser: webdriver.Chrome):
    ''' Purpose: Catch exception if no browser indication of bio text update. '''
    try:
        WebDriverWait(browser, 8).until(EC.text_to_be_present_in_element(
            (By.XPATH, "//p[contains(text(), 'Profile saved.')]"), 'Profile saved.')
        )
    except TimeoutException:
        raise TimeoutException('Failed to verify that bio updated...')

def update_text(browser: webdriver.Chrome, current_text: str):
    ''' Returns: Current bio - will update bio text if out of date. '''
    new_text = build_text()
    if current_text != new_text:
        get_account_details(browser)
        biography_input = browser.find_element(By.CSS_SELECTOR, "textarea[id='pepBio']")
        biography_input.clear()
        biography_input.send_keys(new_text)
        update_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
        update_button.click()
        verify_update(browser)
        Log.status(f'Updated text: {new_text} at {datetime.now()}')
    sleep(randint(1, 2))
    return new_text

if __name__ == '__main__':
    fail = 0
    while fail <= 10:
        environment = sys.argv[1] if len(sys.argv) >= 2 else 'local'
        Log.info(f'Running as: {environment}')
        browser = setup(environment)
        try:
            login(browser)
            current_text = get_current(browser)
            Log.status('Login success!')
            Log.info(f'Current text: {current_text}')
            end_day = calculate_end()
            Log.info(f'Session restarts: {end_day}')
            while True:
                day = date.today()
                if day == end_day:
                    Log.status('Session expired, restarting')
                    browser.quit()
                    break
                current_text = update_text(browser, current_text)
                fail = 0
        except EnvironmentError:
            Log.alert('Set .env file!')
            break
        except KeyboardInterrupt:
            browser.quit()
            break
        except Exception as e:
            Log.error(e)
            Log.trace(e.__traceback__)
            Log.warn(f'Failed: #{fail}')
            browser.quit()
            fail += 1
            sleep(randint(720, 960))
    Log.alert('Process exiting...')
    sys.exit(0)
