import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_checkout():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/login")

    # Log in with the registered account
    email = f"testuser{random.randint(1, 1000)}@yopmail.com"  # Replace with your actual registered email
    password = "Password123"  # Replace with the actual password used during registration

    # Fill in the login form
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    # Wait for the home page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-text"))
    )

    # Search for "Asus"
    search_box = driver.find_element(By.CSS_SELECTOR, "input.search-text")
    search_box.send_keys("Asus")
    search_box.submit()

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )

    # Add two Asus laptops to the cart
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    for i in range(2):  # Adding first two products
        products[i].find_element(By.CSS_SELECTOR, ".button-2.add-to-cart-button").click()
        time.sleep(1)  # Wait briefly to allow the action to complete

    # Go to the cart
    driver.find_element(By.CLASS_NAME, "cart-label").click()

    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "checkout"))
    )
    driver.find_element(By.CLASS_NAME, "checkout").click()

    # Select "Next Day Air" shipping method
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shippingoption_1"))
    )
    driver.find_element(By.ID, "shippingoption_1").click()

    # Continue to payment
    driver.find_element(By.CLASS_NAME, "button-1.shipping-method-next-step-button").click()

    # Fill in payment details (this part might need adjustment based on requirements)
    driver.find_element(By.CLASS_NAME, "button-1.payment-method-next-step-button").click()

    # Verify order completion message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "order-completed"))
    )
    assert "Thank you" in driver.page_source  # Adjust based on actual completion message

    print("Order completed successfully!")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    login_and_checkout()
