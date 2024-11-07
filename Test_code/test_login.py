from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data.data import TestData,TestSelectors

import pytest

class TestOrangeHRM:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestData.url)
        yield
        self.driver.quit()

    def test_valid_login(self, booting_function):
        """Helper function to perform login."""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, TestSelectors.input_box_username))
        
        )
        username_field.clear()
        username_field.send_keys(TestData.username)
        
        password_field = self.driver.find_element(By.NAME, TestSelectors.input_box_password)
        password_field.clear()
        password_field.send_keys(TestData.password)
        
        login_button = self.driver.find_element(By.XPATH, TestSelectors.login_xpath)
        login_button.click()

    def test_invalid_login(self, booting_function):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, TestSelectors.input_box_username))
        )
        username_field.clear()
        username_field.send_keys(TestData.password)
        
        password_field = self.driver.find_element(By.NAME, TestSelectors.input_box_password)
        password_field.clear()
        password_field.send_keys(TestData.password)
        
        login_button = self.driver.find_element(By.XPATH,TestSelectors.login_xpath)
        login_button.click()
        
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,TestSelectors.error_message))
        )
        error_message = error_message_element.text
        assert error_message == TestData.expected_error_message, f"Expected '{TestData.expected_error_message}', but got '{error_message}'"
        print(f"Test Passed: Correct error message displayed - '{error_message}'")

    