import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.headless = True

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    binary = '/home/yernar.kuanyshbay/Downloads/firefox/firefox'
    #driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'./drivers/geckodriver', options=options)
    driver = webdriver.Chrome(r'./drivers/chromedriver', chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)

    yield driver
    driver.quit()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(smoke): mark test to run only on named environment"
    )