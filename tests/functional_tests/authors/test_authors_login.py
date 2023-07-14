import pytest

from selenium.webdriver.common.by import By
from .base import AuthorsBaseTest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(username='my_user', password='pass')

        # User open a login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # See the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # User type your username and password
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # User send the form
        form.submit()

        # User get the successfull login message
        self.assertIn(
            f'You are logged in with {user.username}.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_create_raises_404_if_not_post_method(self):
        self.browser.get(
            self.live_server_url +
            reverse('authors:login_create'))

        self.assertIn(
            'Not Found', self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_is_invalid(self):
        # User open the login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # User see the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And try to send empty values
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('  ')
        password.send_keys('  ')

        # User send the empty form
        form.submit()

        # User see the error message
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_is_a_invalid_credential(self):
        # User open the login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # User see the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And try to send empty values
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('invalid_username')
        password.send_keys('invalid_password')

        # User send the empty form
        form.submit()

        # User see the error message
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
