from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class OrderPage(BasePage):
    DATE_FIELD = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    DROPDOWN_ARROW = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    DROPDOWN_OPTION = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    SCOOTER_COLORS = {
        "black": [By.ID, 'black'],
        "grey": [By.ID, 'grey']
            }
    COMMENT_FOR_COURIER = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]
    ORDER_BTN = [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]"]
    CONFIRMATION_BTN = [By.XPATH, "//button[text()='Да']"]
    success_order_confirmation = [By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]"]

    @allure.step('Заполняем поля в форме об аренде')
    def send_data_about_rent(self, date, duration_rent, color, comment):
        self.do_send_keys(self.DATE_FIELD, date)
        self.do_click(self.DROPDOWN_ARROW)
        self.do_click(self.DROPDOWN_OPTION[duration_rent])
        self.do_click(self.SCOOTER_COLORS[color])
        self.do_send_keys(self.COMMENT_FOR_COURIER, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_button_submit(self):
        self.do_click(self.ORDER_BTN)

    @allure.step('Нажимаем кнопку Да для подтверждения заказа')
    def click_popup_button_confirm(self):
        self.do_click(self.CONFIRMATION_BTN)




