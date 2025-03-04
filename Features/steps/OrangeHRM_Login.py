from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

# Initialize WebDriver
@given('I open the OrangeHRM login page')
def step_open_login_page(context):
    # Initialize and launches the chrome driver
    context.driver = webdriver.Chrome()
    # Launches the URL
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Maximize the Chrome browser
    context.driver.maximize_window()
    # Wait for 2 secs
    sleep(2)

@when('I enter the username "{username}"')
def step_enter_username(context, username):
    # context --> Used to interact with the elements of the webpage
    username_field = context.driver.find_element(By.NAME, "username")
    username_field.send_keys(username)
    sleep(1)

@when('I enter the password "{password}"')
def step_enter_password(context, password):
    password_field = context.driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    sleep(1)

@when('I click the login button')
def step_click_login(context):
    login_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(3)

@then('I should be redirected to the dashboard')
def step_verify_dashboard(context):
    assert "dashboard" in context.driver.current_url.lower(), "Login failed"
    context.driver.quit()
