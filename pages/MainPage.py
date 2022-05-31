import time
import requests
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators:
    LOCATOR_Auth_button = (By.XPATH, "//button[@data-testid='CButton']//span[text() = 'Войти']")
    LOCATOR_login_form = (By.XPATH, "//*[@data-testid='TLoginForm']")
    LOCATOR_dialog = (By.XPATH, "//div[@role='dialog']")
    LOCATOR_excape = (By.XPATH, "//div[@role='none presentation']")
    LOCATOR_phone_input = (By.XPATH, "//input[@id='TLoginForm-mobilePhone']")
    LOCATOR_continue_button = (By.XPATH, "//span[text() = 'Продолжить']")
    LOCATOR_passwordField_button = (By.XPATH, "//input[@name='password']")

class MainPageDates:
    phone = "77089378518"
    password = "Some"

class MainPageHelper(BasePage):
    def authorization(self):
        r = requests.get('https://home-api.centerhome.kz/estate-api/v1/estate/')
        data = r.status_code
        print(data)
        dialog_window = self.find_element(MainPageLocators.LOCATOR_dialog, time=2)
        excape = self.find_element(MainPageLocators.LOCATOR_excape, time=2)
        if dialog_window.is_displayed():
            print("Element found")
            excape.click()
        auth_button = self.find_element(MainPageLocators.LOCATOR_Auth_button, time=2)
        auth_button.click()

        login_form = self.find_element(MainPageLocators.LOCATOR_login_form, time=2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(login_form))

        phone_input = self.find_element(MainPageLocators.LOCATOR_phone_input, time=2)
        phone_input.send_keys(MainPageDates.phone)

        continue_button = self.find_element(MainPageLocators.LOCATOR_continue_button, time=2)
        continue_button.click()

        passwordField_button = self.find_element(MainPageLocators.LOCATOR_passwordField_button, time=2)
        passwordField_button.send_keys(MainPageDates.password)

        continue_button = self.find_element(MainPageLocators.LOCATOR_continue_button, time=2)
        continue_button.click()








