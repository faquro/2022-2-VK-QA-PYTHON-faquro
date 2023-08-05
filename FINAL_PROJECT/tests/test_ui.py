import datetime

import allure
import pytest

from .base import BaseCase
from .static import ADMIN_USER, ADMIN_PASSWORD, ADMIN_EMAIL, VK_ID_ADMIN


class TestAuthorization(BaseCase):
    """Тесты страницы авторизации"""
    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with correct data')
    @pytest.mark.UI
    def test_correct_login(self):
        username, password = ADMIN_USER, ADMIN_PASSWORD
        self.base_page.login(username, password)
        assert f'Logged as {ADMIN_USER}' in self.driver.page_source
        assert self.mysql_builder.is_active(username)

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with incorrect login')
    @pytest.mark.UI
    def test_incorrect_login(self, random_string):
        username, password = random_string, ADMIN_PASSWORD
        self.base_page.login(username, password)
        assert 'Invalid username or password'

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with incorrect password')
    @pytest.mark.UI
    def test_incorrect_pass(self, random_string):
        username, password = ADMIN_USER, random_string
        self.base_page.login(username, password)
        assert 'Invalid username or password'


class TestRegistration(BaseCase):
    """Тесты страницы регистрации"""
    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Checking input field names')
    @pytest.mark.parametrize('loc', [0, 1, 2, 3, 4, 5, 6])
    @pytest.mark.UI
    def test_check_fields(self, userdata, loc):
        title = ['Name', 'Surname', 'Middlename', 'Username', 'Email', 'Password', 'Repeat password']
        self.base_page.go_to_registration()
        placeholder_name = self.registration_page.find_input(loc).get_attribute('placeholder')
        assert placeholder_name == title[loc]

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with correct data')
    @pytest.mark.UI
    def test_correct_registration(self, userdata):
        self.registration_page.register(userdata)
        assert f'Logged as {userdata["username"]}' in self.driver.page_source
        assert self.mysql_builder.user_exists(userdata["username"])

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with too long name')
    @pytest.mark.UI
    def test_incorrect_name_length(self, userdata):
        userdata['name'] = 'vk' * 300
        self.registration_page.register(userdata)
        assert f'Incorrect name length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with too long surname')
    @pytest.mark.UI
    def test_incorrect_surname_length(self, userdata):
        userdata['surname'] = 'vk' * 300
        self.registration_page.register(userdata)
        assert f'Incorrect surname length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with too long middlename')
    @pytest.mark.UI
    def test_incorrect_middle_name_length(self, userdata):
        userdata['middle_name'] = 'vk' * 300
        self.registration_page.register(userdata)
        assert f'Incorrect middlename length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with invalid username')
    @pytest.mark.UI
    @pytest.mark.parametrize('invalid_username', ['vk', 'vk22' * 20])
    def test_incorrect_username_lenght(self, userdata, invalid_username):
        userdata['username'] = invalid_username
        self.registration_page.register(userdata)
        assert self.registration_page.is_registration_page()

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with wrong symbols in password')
    @pytest.mark.UI
    def test_incorrect_password_symbols(self, userdata):
        userdata['password'] = 'øŋғçŋғçø'
        userdata['pass_repeat'] = userdata['password']
        self.registration_page.register(userdata)
        assert f'Password has incorrect symbols' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with too long password')
    @pytest.mark.UI
    def test_incorrect_password_length(self, userdata):
        userdata['password'] = 'vk' * 200
        userdata['pass_repeat'] = userdata['password']
        self.registration_page.register(userdata)
        assert f'Incorrect password length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with incorrect email')
    @pytest.mark.UI
    @pytest.mark.parametrize('invalid_email', ['vkvkvk', '@myapp.ru', '.vk@myapp.ru'])
    def test_incorrect_email(self, userdata, invalid_email):
        userdata['email'] = invalid_email
        self.registration_page.register(userdata)
        assert f'Invalid email address' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with already existed email')
    @pytest.mark.UI
    def test_exist_email(self, userdata):
        userdata['email'] = ADMIN_EMAIL
        self.registration_page.register(userdata)
        assert f'This email is already in use' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with invalid email length')
    @pytest.mark.UI
    def test_invalid_email_length(self, userdata):
        userdata['email'] = 'vk' * 100 + '@myapp.ru'
        self.registration_page.register(userdata)
        assert f'Incorrect email length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with different password and confirmation')
    @pytest.mark.UI
    def test_different_password_confirmation(self, userdata, random_string):
        userdata['pass_repeat'] = random_string
        self.registration_page.register(userdata)
        assert f'Passwords must match' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register without accept')
    @pytest.mark.UI
    def test_if_not_accept(self, userdata):
        self.registration_page.register_without_accept(userdata)
        assert self.registration_page.is_registration_page()

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with empty required fields')
    @pytest.mark.UI
    @pytest.mark.parametrize('empty_field', ['username', 'password', 'email', 'pass_repeat'])
    def test_empty_fields(self, userdata, empty_field):
        userdata[empty_field] = ''
        self.registration_page.register(userdata)
        assert self.registration_page.is_registration_page()

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Go to login page')
    @pytest.mark.UI
    def test_go_to_login(self):
        self.registration_page.go_to_login()
        assert self.driver.current_url == \
               f'http://myapp_final_project:8082/login'


class TestMainPage(BaseCase):
    """Тесты гоавной страницы"""

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to api page')
    @pytest.mark.UI
    def test_go_to_api(self):
        self.account_page.go_to_api()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://en.wikipedia.org/wiki/API'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to internet page')
    @pytest.mark.UI
    def test_go_to_internet(self):
        self.account_page.go_to_internet()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == "https://www.popularmechanics.com/technology/infrastructure/a29666802" \
                                          "/future-of-the-internet/"

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to SMTP page')
    @pytest.mark.UI
    def test_go_to_smtp(self):
        self.account_page.go_to_smtp()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == "https://ru.wikipedia.org/wiki/SMTP"

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to home page')
    @pytest.mark.UI
    def test_go_to_home(self):
        self.account_page.go_to_home()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == f'http://myapp_final_project:8082/welcome/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to python page')
    @pytest.mark.UI
    def test_go_to_python(self):
        self.account_page.go_to_python()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://www.python.org/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to python history page')
    @pytest.mark.UI
    def test_go_to_python_history(self):
        self.account_page.go_to_python_history()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://en.wikipedia.org/wiki/History_of_Python'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to flask page')
    @pytest.mark.UI
    def test_go_to_flask(self):
        self.account_page.go_to_flask()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://flask.palletsprojects.com/en/1.1.x/#'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to Centos page')
    @pytest.mark.UI
    def test_go_to_centos(self):
        self.account_page.go_to_centos()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert 'Download Centos7' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to news page')
    @pytest.mark.UI
    def test_go_to_news(self):
        self.account_page.go_to_news()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://www.wireshark.org/news/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to download page')
    @pytest.mark.UI
    def test_go_to_download(self):
        self.account_page.go_to_download()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://www.wireshark.org/#download'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to examples page')
    @pytest.mark.UI
    def test_go_to_examples(self):
        self.account_page.go_to_examples()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://hackertarget.com/tcpdump-examples/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Check vk api on page')
    @pytest.mark.UI
    def test_vk_id_appear(self):
        assert f'VK ID: {VK_ID_ADMIN}' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Check date in footer')
    @pytest.mark.UI
    def test_footer_date(self):
        self.account_page.go_to_home()
        current_year = datetime.datetime.now().year
        assert f'Powered by VK Education © 2020 - {current_year}' in self.driver.page_source
