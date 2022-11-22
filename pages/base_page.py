from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_for_tests import users
from data_for_tests import urls

""""Это родительский класс для всех страниц. В нем содержатся базовые методы."""

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(urls.Urls.base_url)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))
        return self.driver.current_url
