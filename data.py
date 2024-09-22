class URL:

    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = f'{MAIN_PAGE}/login'
    PROFILE_PAGE = f'{MAIN_PAGE}/account/profile'
    RESET_PASSWORD = f'{MAIN_PAGE}/reset-password'
    HISTORY_PAGE = f'{MAIN_PAGE}/account/order-history'
    FEED_PAGE = f'{MAIN_PAGE}/feed'
    RECOVERY_PAGE = f'{MAIN_PAGE}/forgot-password'


class Ingredients:
    BUN_CRATOR = '61c0c5a71d1f82001bdaaa6c'
    FILLING_TETRA = '61c0c5a71d1f82001bdaaa6e'
    SAUCE_ANTARIAN = '61c0c5a71d1f82001bdaaa75'


class API:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register'
    LOGIN_USER = f'{MAIN_PAGE}/api/auth/login'
    DELETE_DATA = f'{MAIN_PAGE}/api/auth/user'
    CREATE_ORDER = f'{MAIN_PAGE}/api/orders'
