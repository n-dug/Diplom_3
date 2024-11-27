from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_CONSTRUCTOR = By.XPATH, "//h1[text()='Соберите бургер']"
    ACCOUNT_BUTTON = By.XPATH, (".//p[contains(@class, 'AppHeader_header__linkText') "
                                "and text()='Личный Кабинет']")
    COUNTER_BUN = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    BUN_ITEM = By.XPATH, "//p[text()='Краторная булка N-200i']"
    HEADER_LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    ADD_SECTION = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"
    CREATE_ORDER_POP_UP = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
    HEADER_POP_UP = By.XPATH, "//h2[text()='Детали ингредиента']"
    CLOSE_POP_UP_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"
    CLOSE_POP_UP = By.CLASS_NAME, "Modal_modal__P3_V5"
    HEADER_CREATE_ORDER_POP_UP = By.XPATH, "//p[text()='идентификатор заказа']"
