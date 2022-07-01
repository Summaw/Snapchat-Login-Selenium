import json
import os
import asyncio
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class Clickable:
    def __init__(self, driver):
        self.driver = driver

    def clickable(self, path, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, path)))
        

class SnapChat:    
    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-web-security")
        options.add_argument("--log-level=3")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--start-maximized')
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver
    
    async def main(self):
        driver = self.create_driver()
        driver.get("https://accounts.snapchat.com/accounts/login?client_id=ads-api&referrer=https%253A%252F%252Fads.snapchat.com%252Fgetstarted&ignore_welcome_email=true")
        c = Clickable(driver)
        #sleep(100)
        c.clickable("//input[@name='username']").send_keys('Username')
        c.clickable("//input[@name='password']").send_keys('password')
        sleep(5)
        #Captcha stuff here might add solver later
        c.clickable("//button[@type='submit']").click()

asyncio.run(SnapChat().main())

