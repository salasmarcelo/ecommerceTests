# Selenium E-commerce Test Suite

This test suite demonstrates automated testing of an e-commerce website (Amazon) using the Selenium WebDriver framework. The suite includes tests for adding a product to the cart, removing a product from the cart, and checking product ratings.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- ChromeDriver (or the appropriate WebDriver for your preferred browser)

## Setup

1. Install the required packages:

   ```bash
   pip install selenium webdriver-manager

## Running the Tests
1. Open a terminal or command prompt.

2. Navigate to the directory containing the test script.

3. Run the test script using the following command:

    ```bash
    python ecommerceTests.py

## Test Cases

### Test 1: Adding Product to Cart
This test case verifies the ability to add a product to the cart on the e-commerce website.

Steps:

1. Navigate to the Amazon homepage.
2. Search for a product (e.g., "Laptop").
3. Click on a product link.
4. Retrieve the product title.
5. Click the "Add to Cart" button.
6. Handle pop-ups.
7. Navigate to the cart.
8. Verify the product is present in the cart.

### Test 2: Removing Product from Cart
This test case verifies the ability to remove a product from the cart on the e-commerce website.

Steps:
1. Repeat steps 1-6 from the previous test case.
2. Navigate to the cart.
3. Click the "Delete" button to remove the product.
4. Verify the cart is empty after removal.

### Test 3: Checking Product Rating
This test case verifies the display of product ratings on the e-commerce website.

1. Repeat steps 1-5 from the previous test cases.
2. Locate the element displaying the product rating.
3. Verify the rating is present

### Tear Down
After each test case, the browser instance will be closed.

## Demo Video

https://github.com/salasmarcelo/ecommerceTests/assets/141787326/f1e25e9e-2861-42c9-b207-92db385d931d

