from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = By.XPATH, (".//p[contains(@class, 'AppHeader_header__linkText') "
                                "and text()='Личный Кабинет']")
    LOG_IN_BUTTON = By.XPATH, ".//button[text()='Войти']"
    NUMBER_ORDER_BLOCK = By.XPATH, "//p[contains(@class, 'text_type_digits')]"
    USER_HISTORY_MENU = By.XPATH, "//a[text()='История заказов']"
    ORDER_WITH_NUMBER_ORDER_BLOCKS = By.XPATH, (".//div[contains(@class, 'OrderHistory_textBox')]"
                                                "/p[@class='text text_type_digits-default']")
    LOG_OUT_MENU = By.XPATH, "//button[text()='Выход']"
