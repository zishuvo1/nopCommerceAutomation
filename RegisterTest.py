import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_user():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/register")

    email = f"testuser{random.randint(1, 1000)}@yopmail.com"

    driver.find_element(By.ID, "FirstName").send_keys("Test")
    driver.find_element(By.ID, "LastName").send_keys("User")
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Password123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Password123")
    driver.find_element(By.ID, "register-button").click()

    time.sleep(3)  # Wait for a few seconds after clicking register

    # Update the selector based on the actual HTML structure
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "result"))  # Update as needed
        )

        assert "Your registration completed" in driver.page_source, "Registration failed!"

        print("Registration successful with email:", email)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.quit()

if __name__ == "__main__":
    register_user()
