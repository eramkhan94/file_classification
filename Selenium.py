from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize driver
service = Chrome_Service(binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://iam.intralinks.com/idp/login...")

    # Use a more flexible XPath to find the email input field
    # This looks for an input inside the il-framework-component container
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@data-type='text' or @type='email']"))
    )
    email_field.send_keys("eram.khan@hsbc.co.in")

    # Target the 'Next' button using its text content
    next_button = driver.find_element(By.XPATH, "//button[contains(., 'Next')]")
    next_button.click()

except Exception as e:
    print(f"An error occurred: {e}")
