from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data_for_tests import urls
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(urls.Urls)

    questions = {
        1: [By.ID, 'accordion__heading-0'],
        2: [By.ID, 'accordion__heading-1'],
        3: [By.ID, 'accordion__heading-2'],
        4: [By.ID, 'accordion__heading-3'],
        5: [By.ID, 'accordion__heading-4'],
        6: [By.ID, 'accordion__heading-5'],
        7: [By.ID, 'accordion__heading-6'],
        8: [By.ID, 'accordion__heading-7']
    }

    answers = {
        1: [By.ID, 'accordion__panel-0'],
        2: [By.ID, 'accordion__panel-1'],
        3: [By.ID, 'accordion__panel-2'],
        4: [By.ID, 'accordion__panel-3'],
        5: [By.ID, 'accordion__panel-4'],
        6: [By.ID, 'accordion__panel-5'],
        7: [By.ID, 'accordion__panel-6'],
        8: [By.ID, 'accordion__panel-7'],
    }

    COOKIE_BTN = [By.ID, 'rcc-confirm-button']
    ORDER_BTN_HEADER = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    ORDER_BTN_MIDDLE = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    LOGO_SCOOTER = [By.CSS_SELECTOR, '[alt = "Scooter"]']
    LOGO_YANDEX = [By.CSS_SELECTOR, '[alt = "Yandex"]']

    @allure.step('Принимаем условия по кукам')
    def click_cookie_button(self):
        self.do_click(self.COOKIE_BTN)

    @allure.step('Прокручиваем страницу вниз')
    def scroll_to_the_bottom_main_page(self):
        self.scroll_to_the_bottom()

    @allure.step('Нажимаем на кнопку с вопросом')
    def click_question_btn(self, number_btn):
        self.do_click(self.questions[number_btn])

    @allure.step('Получаем текст кнопки с вопросом')
    def get_question_btn_text(self, number_btn):
        return self.get_element_text(self.questions[number_btn])

    @allure.step('Получаем текст кнопки с ответом')
    def get_answer_btn_text(self, number_btn):
        return self.get_element_text(self.answers[number_btn])

    @allure.step('Нажимаем кнопку Заказать в хедере')
    def click_order_button_header(self):
        self.do_click(self.ORDER_BTN_HEADER)

    @allure.step('Нажимаем кнопку Заказать в центре страницы')
    def click_order_button_middle(self):
        self.do_click(self.ORDER_BTN_MIDDLE)

    @allure.step('Нажимаем логотип Самокат')
    def click_logo_scooter(self):
        self.do_click(self.LOGO_SCOOTER)

    @allure.step('Нажимаем логотип Yandex')
    def click_logo_yandex(self, tab):
        self.do_click(self.LOGO_YANDEX)
        window_after = self.driver.window_handles[tab]
        self.driver.switch_to.window(window_after)