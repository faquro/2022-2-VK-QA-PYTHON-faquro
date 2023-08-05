from selenium.webdriver.common.by import By


class Login_Page_Locators:
    LOGIN_BUTTON = (By.XPATH, "//input[contains(@class, 'uk-button')]")
    LOGIN_INPUT = (By.XPATH, '//input[@class="uk-input uk-form-large"]')
    PASS_INPUT = (By.XPATH, "//input[contains(@class, 'uk-input uk-form-large uk-icon-eye')]")
    CREATE_ACC_LINK = (By.XPATH, '//a[@href="/reg"]')
    USER_MIDDLE_NAME_INPUT = (By.XPATH, "//input[@id='user_middle_name']")


class Registration_Page_Locators:
    CREATE_ACC_LINK = (By.XPATH, '//a[@href="/reg"]')
    USER_NAME_INPUT = (By.XPATH, "//input[@id='user_name']")
    USER_SURNAME_INPUT = (By.XPATH, "//input[@id='user_surname']")
    USER_MIDDLE_NAME_INPUT = (By.XPATH, "//input[@id='user_middle_name']")
    USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    REPEAT_PASS_INPUT = (By.XPATH, "//input[@name='confirm']")
    EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    ACCEPT = (By.XPATH, '//input[@id="term"]')
    REGISTER_BUTTON = (By.XPATH, "//input[contains(@class, 'uk-button')]")
    GO_TO_LOGIN_LINK = (By.XPATH, '//a[@href="/login"]')


class Account_Page_Locators:
    GO_TO_API_LINK = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    GO_TO_INTERNET_LINK = (By.XPATH,
                           '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of'
                           '-the-internet/"]')
    GO_TO_SMTP_LINK = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')
    LOGOUT_LINK = (By.XPATH, '//a[@href="/logout"]')
    HOME_LINK = (By.XPATH, '//a[@href="/"]')
    PYTHON_LINK = (By.XPATH, '//a[contains(text(),"Python")]')
    PYTHON_HISTORY_LINK = (By.XPATH, '//a[contains(text(),"Python history")]')
    FLASK_LINK = (By.XPATH, '//a[@href="https://flask.palletsprojects.com/en/1.1.x/#"]')
    LINUX_LINK = (By.XPATH, '//a[contains(text(),"Linux")]')
    CENTOS_LINK = (By.XPATH, '//a[@href="https://getfedora.org/ru/workstation/download/"]')
    NETWORK_LINK = (By.XPATH, '//a[contains(text(),"Network")]')
    NEWS_LINK = (By.XPATH, '//a[@href="https://www.wireshark.org/news/"]')
    DOWNLOAD_LINK = (By.XPATH, '//a[@href="https://www.wireshark.org/#download"]')
    EXAMPLES_LINK = (By.XPATH, '//a[@href="https://hackertarget.com/tcpdump-examples/"]')
