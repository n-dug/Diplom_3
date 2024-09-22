from selenium.webdriver.common.by import By


class ResetPageLocators:

    HEADER_RECOVERY_PAGE = By.XPATH, "//h2[text()='Восстановление пароля']"
    RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/../input"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    PASSWORD_INPUT_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"
    EYE_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]"
