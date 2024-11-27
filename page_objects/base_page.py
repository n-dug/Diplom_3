from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_all_element(self, locator):
        self.wait_element_presence_of_element_located(locator)
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def drag_drop(self, locator_from, locator_to):
        ActionChains(self.driver).drag_and_drop(
            self.find_element(locator_from),
            self.find_element(locator_to)
        ).perform()

    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    def wait_element_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(locator))

    def wait_element_presence_of_all_elements_located(self, locator):
        WebDriverWait(self.driver, 15).until(ec.presence_of_all_elements_located(locator))

    def wait_element_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))

    def wait_element_visibility_of(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of(locator))

    def get_text(self, locator):
        return self.find_element(locator).text

    def switch_to_window(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])
