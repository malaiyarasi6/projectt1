# Test_Data.py

class TestSelectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    error_message='//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'

class TestData:
    username = "Admin"
    password = "admin123"
    url = "https://opensource-demo.orangehrmlive.com"
    expected_error_message="Invalid credentials"