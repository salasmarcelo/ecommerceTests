import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com")
    def test_add_product_to_cart(self):
        # Test 1: Adding Product to Cart and Confirm the Product Name
        wait = WebDriverWait(self.driver, 3)
        try:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)
        except:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "nav-bb-search")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)

        product_link = self.driver.find_element(By.XPATH, "//img[@data-image-index=3]")
        product_link.click()
        product_title = self.driver.find_element(By.ID, "productTitle").text
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        
        wait = WebDriverWait(self.driver, 3)
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Go to Cart')]")))
            cart_button.click()
        except:
            protection_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'No Thanks')]/parent::*")
            protection_button.click()
        try:
            wait = WebDriverWait(self.driver, 3)
            cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
            cart_button.click()
        except:
            try:
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "attach-close_sideSheet-link")))
                cart_button.click()
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
                cart_button.click()
            except:
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
                cart_button.click()
        
        product_title_in_cart = self.driver.find_element(By.CSS_SELECTOR, ".sc-product-title").text
        expected_substring = product_title[:10]
        self.assertIn(expected_substring.lower(), product_title_in_cart.lower(), "Product not found in the cart")
    
    def test_remove_product_from_cart(self):
        # Test 2: Removing Product from Cart
        wait = WebDriverWait(self.driver, 3)
        try:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)
        except:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "nav-bb-search")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)

        product_link = self.driver.find_element(By.XPATH, "//img[@data-image-index=3]")
        product_link.click()
        product_title = self.driver.find_element(By.ID, "productTitle").text
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        
        wait = WebDriverWait(self.driver, 3)
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Go to Cart')]")))
            cart_button.click()
        except:
            protection_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'No Thanks')]/parent::*")
            protection_button.click()
        try:
            wait = WebDriverWait(self.driver, 3)
            cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
            cart_button.click()
        except:
            try:
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "attach-close_sideSheet-link")))
                cart_button.click()
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
                cart_button.click()
            except:
                wait = WebDriverWait(self.driver, 3)
                cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
                cart_button.click()
        wait = WebDriverWait(self.driver, 3)        
        remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Delete']")))
        remove_button.click()
        time.sleep(2)
        empty_cart_message = self.driver.find_element(By.ID, "sc-subtotal-label-activecart").text
        self.assertIn("(0 items)", empty_cart_message.lower(), "Product not removed from cart")

    def test_rating(self):
        # Test 3: Confirm that Product Rating is Present
        wait = WebDriverWait(self.driver, 3)
        try:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)
        except:
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "nav-bb-search")))
            search_box.send_keys("Laptop")
            search_box.send_keys(Keys.ENTER)
        product_link = self.driver.find_element(By.XPATH, "//img[@data-image-index=3]")
        product_link.click()
        ratingElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-hook='rating-out-of-text']")))
        rating = ratingElement.text
        self.assertIn("out of", rating.lower(), "Rating Not Present")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
