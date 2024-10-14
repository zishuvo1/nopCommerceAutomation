import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def product_compare():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com")

    # Wait for the page to load
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

    # Add the first Asus product to the compare list
    first_asus_product = driver.find_elements(By.CSS_SELECTOR, ".product-item")[0]
    first_asus_product.find_element(By.CLASS_NAME, "button-2.add-to-compare-list-button").click()
    
    # Wait briefly to allow the action to complete
    time.sleep(1)

    # Now add "HP Envy 6-1180ca 15.6-Inch Sleekbook" from the Notebooks section
    driver.get("https://demo.nopcommerce.com/computers")
    
    # Wait for the Computers page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Notebooks"))
    )
    
    # Click on Notebooks
    driver.find_element(By.LINK_TEXT, "Notebooks").click()

    # Wait for Notebooks page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )

    # Find and add the specific HP laptop to the compare list
    hp_product = driver.find_element(By.LINK_TEXT, "HP Envy 6-1180ca 15.6-Inch Sleekbook")
    hp_product.find_element(By.CLASS_NAME, "button-2.add-to-compare-list-button").click()
    
    # Go to the product comparison page
    driver.find_element(By.LINK_TEXT, "product comparison").click()

    # Wait for the comparison page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".compare-products"))
    )

    # Check for mismatched product information
    compare_table = driver.find_element(By.CSS_SELECTOR, ".compare-products")
    rows = compare_table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        print(row.text)  # Print each row for comparison

    # Here, you would implement logic to verify mismatched information
    # For example, checking expected vs actual values
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    product_compare()
