import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get("https://www.amazon.com")

    def test_add_product_to_cart(self):
        # Test 1: Adding Product to Cart
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.ENTER)

        product_link = self.driver.find_element(By.XPATH, "//div[@data-asin]/div[2]/div/a")
        product_link.click()

        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        product_title_in_cart = self.driver.find_element(By.CSS_SELECTOR, ".sc-product-title").text
        expected_product_title = "Product Name"  # Replace with the actual expected product title
        self.assertIn(expected_product_title, product_title_in_cart, "Product not found in the cart")

    def test_remove_product_from_cart(self):
        # Test 2: Removing Product from Cart
        remove_button = self.driver.find_element(By.XPATH, "//input[@value='Delete']")
        remove_button.click()

        empty_cart_message = self.driver.find_element(By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty").text
        self.assertIn("Your Amazon Cart is empty", empty_cart_message, "Cart is not empty after removing product")

    def test_verify_subtotal_calculation(self):
        # Test 3: Verifying Subtotal Calculation
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        product_prices = self.driver.find_elements(By.CSS_SELECTOR, ".sc-product-price")
        total_price = sum([float(price_element.text.strip("$")) for price_element in product_prices])

        subtotal_element = self.driver.find_element(By.CSS_SELECTOR, ".sc-subtotal-amount-activecart")
        subtotal = float(subtotal_element.text.strip("$"))

        self.assertEqual(total_price, subtotal, "Subtotal does not match the sum of product prices")
    
    def test_verify_shipping_options(self):
        # Test 4: Verifying Shipping Options
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Click on the "Proceed to checkout" button to reach the checkout page
        proceed_to_checkout_button = self.driver.find_element(By.NAME, "proceedToCheckout")
        proceed_to_checkout_button.click()

        # Find the available shipping options
        shipping_options = self.driver.find_elements(By.CSS_SELECTOR, ".a-radio .a-label")

        # List of expected shipping options (replace with actual options)
        expected_shipping_options = ["Standard Shipping", "Expedited Shipping", "Two-Day Shipping"]

        # Check if the expected shipping options match the available options
        for option in shipping_options:
            option_text = option.text
            self.assertIn(option_text, expected_shipping_options, f"Unexpected shipping option: {option_text}")
    
    def test_change_quantity_in_cart(self):
        # Test 5: Changing Quantity in Cart
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        quantity_input = self.driver.find_element(By.NAME, "quantity")
        quantity_input.clear()
        new_quantity = 3  # Replace with the desired new quantity
        quantity_input.send_keys(str(new_quantity))
        quantity_input.send_keys(Keys.ENTER)

        subtotal_element = self.driver.find_element(By.CSS_SELECTOR, ".sc-subtotal-amount-activecart")
        subtotal = float(subtotal_element.text.strip("$"))

        product_price = float(self.driver.find_element(By.CSS_SELECTOR, ".sc-product-price").text.strip("$"))

        expected_subtotal = new_quantity * product_price
        self.assertEqual(expected_subtotal, subtotal, "Subtotal does not match the new quantity's total price")

    def test_apply_coupon_code(self):
        # Test 2: Applying Coupon Code
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Apply coupon code (replace with the actual coupon code)
        coupon_input = self.driver.find_element(By.ID, "coupon-code")
        coupon_input.send_keys("COUPONCODE")
        apply_coupon_button = self.driver.find_element(By.ID, "apply-coupon-button")
        apply_coupon_button.click()

        # Check if the discounted price is reflected in the subtotal
        expected_discounted_subtotal = 100.0  # Replace with the expected discounted subtotal
        subtotal_element = self.driver.find_element(By.CSS_SELECTOR, ".sc-subtotal-amount-activecart")
        actual_subtotal = float(subtotal_element.text.strip("$"))
        self.assertEqual(expected_discounted_subtotal, actual_subtotal, "Discounted subtotal is incorrect")

    def test_invalid_coupon_code(self):
        # Test 7: Applying Invalid Coupon Code
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Apply an invalid coupon code
        coupon_input = self.driver.find_element(By.ID, "coupon-code")
        coupon_input.send_keys("INVALIDCODE")
        apply_coupon_button = self.driver.find_element(By.ID, "apply-coupon-button")
        apply_coupon_button.click()

        # Check for error message
        error_message = self.driver.find_element(By.ID, "coupon-error-message").text
        expected_error_message = "Invalid coupon code"  # Replace with the actual expected error message
        self.assertEqual(expected_error_message, error_message, "Unexpected error message")

    def test_continue_shopping_button(self):
        # Test 9: Continue Shopping Button
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Click the "Continue Shopping" button
        continue_shopping_button = self.driver.find_element(By.CSS_SELECTOR, ".sc-continue-button .a-button-input")
        continue_shopping_button.click()

        # Verify that the user is redirected to the shopping page
        shopping_page_title = "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
        self.assertEqual(shopping_page_title, self.driver.title, "Not redirected to shopping page")

    def test_edit_cart_items(self):
        # Test 11: Edit Cart Items
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Click on "Edit" to change the quantity of the item
        edit_link = self.driver.find_element(By.LINK_TEXT, "Edit")
        edit_link.click()

        new_quantity_input = self.driver.find_element(By.NAME, "quantity")
        new_quantity = 2  # Replace with the desired new quantity
        new_quantity_input.clear()
        new_quantity_input.send_keys(str(new_quantity))
        update_button = self.driver.find_element(By.NAME, "save")
        update_button.click()

        # Verify that the quantity has been updated
        updated_quantity = self.driver.find_element(By.CSS_SELECTOR, ".sc-quantity-update-message").text
        self.assertIn(str(new_quantity), updated_quantity, "Quantity not updated")

    def test_save_for_later(self):
        # Test 10: Save for Later
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Click on "Save for later"
        save_for_later_link = self.driver.find_element(By.LINK_TEXT, "Save for later")
        save_for_later_link.click()

        # Verify that the item is saved for later
        saved_for_later_message = self.driver.find_element(By.CSS_SELECTOR, ".sc-saved-for-later-message").text
        self.assertIn("Saved for later", saved_for_later_message, "Not saved for later")

    def test_multiple_products(self):
        # Test 12: Multiple Products in Cart
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        # Add a second product
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("Shirt")  # Replace with the desired second product
        search_box.send_keys(Keys.ENTER)

        second_product_link = self.driver.find_element(By.XPATH, "//div[@data-asin]/div[2]/div/a")
        second_product_link.click()

        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        cart_button = self.driver.find_element(By.ID, "nav-cart")
        cart_button.click()

        # Verify that both products are in the cart
        product_titles_in_cart = self.driver.find_elements(By.CSS_SELECTOR, ".sc-product-title")
        expected_product_titles = ["Product 1", "Product 2"]  # Replace with actual product titles
        for title_element, expected_title in zip(product_titles_in_cart, expected_product_titles):
            self.assertIn(expected_title, title_element.text, f"Product '{expected_title}' not found in cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
