import allure
import pytest

from pages.MainPage import MainPageHelper

@allure.feature('Авторизация на платформе')
@allure.severity('blocker')
@pytest.mark.smoke
def test_auth(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.authorization()
