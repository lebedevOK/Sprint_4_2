from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class UserPage(BasePage):
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    LASTNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    STATION_SELECTED = [By.CSS_SELECTOR, '[class="select-search__select"]']
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    CONTINUE_BTN = [By.XPATH, "//button[text()='Далее']"]

    @allure.step('Заполняем поля в форме Для кого самокат')
    def send_data_about_customer(self, name, lastname, address, station, phone):
        self.do_send_keys(self.NAME_FIELD, name)
        self.do_send_keys(self.LASTNAME_FIELD, lastname)
        self.do_send_keys(self.ADDRESS_FIELD, address)
        self.do_send_keys(self.STATION_FIELD, station)
        self.do_click(self.STATION_SELECTED)
        self.do_send_keys(self.PHONE_FIELD, phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_continue_button(self):
        self.do_click(self.CONTINUE_BTN)