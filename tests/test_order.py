from pages.maine_page import MainPage
from pages.user_page import UserPage
from pages.order_page import OrderPage
import time
import allure

from data_for_tests.urls import Urls
from data_for_tests.users import Users

class TestCustomerRent:

    @allure.title('Проходим сценарий заказа через хедер')
    def test_order_from_header_success(self, driver):
        main_page = MainPage(driver)
        customer_page = UserPage(driver)
        rent_page = OrderPage(driver)
        main_page.click_cookie_button()
        main_page.click_order_button_header()
        customer_page.send_data_about_customer(
            Users.USER_ONE['name'],
            Users.USER_ONE['lastname'],
            Users.USER_ONE['address'],
            Users.USER_ONE['subway_station'],
            Users.USER_ONE['phone']
        )
        customer_page.click_continue_button()

        rent_page.send_data_about_rent(
            Users.USER_ONE['date'],
            Users.USER_ONE['duration_rent'],
            Users.USER_ONE['color'],
            Users.USER_ONE['comment']
        )
        rent_page.click_button_submit()
        rent_page.click_popup_button_confirm()
        time.sleep(1)
        assert driver.find_element(OrderPage.success_order_confirmation)

    @allure.title('Проходим сценарий заказа через блок Как это работает')
    def test_order_from_middle_section(self, driver):
        main_page = MainPage(driver)
        customer_page = UserPage(driver)
        rent_page = OrderPage(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_order_button_middle()
        customer_page.send_data_about_customer(
            Users.USER_TWO['name'],
            Users.USER_TWO['lastname'],
            Users.USER_TWO['address'],
            Users.USER_TWO['subway_station'],
            Users.USER_TWO['phone']
        )
        customer_page.click_continue_button()

        rent_page.send_data_about_rent(
            Users.USER_TWO['date'],
            Users.USER_TWO['duration_rent'],
            Users.USER_TWO['color'],
            Users.USER_TWO['comment']
        )
        rent_page.click_button_submit()
        rent_page.click_popup_button_confirm()
        time.sleep(1)
        assert driver.find_element(OrderPage.success_order_confirmation)

class TestRedirectingButtons:

    @allure.title("Переход на главную страницу Самоката по кнопке лого со страницы Заказа")
    def test_go_to_scooter_page_from_logo(self, driver):
        scooter_page = MainPage(driver)
        scooter_page.click_logo_scooter()
        assert driver.current_url == Urls.base_url

    @allure.title("Переход на главную страницу Яндекса по клику на лого")
    def test_go_to_yandex_page_from_logo(self, driver):
        yandex_page = MainPage(driver)
        yandex_page.click_logo_yandex()
        assert driver.current_url == Urls.ya_dz_url
        #assert self.driver.current_url.startswith('https://dzen.ru/?yredirect=true')








