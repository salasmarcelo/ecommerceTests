# Test Case Documentation: E-commerce Shopping Cart Testing

## Table of Contents
1. [Introduction](#introduction)
2. [Test Environment Setup](#test-environment-setup)
3. [Test Case Descriptions](#test-case-descriptions)
    - [Test Case 1: Adding Product to Cart](#test-case-1-adding-product-to-cart)
    - [Test Case 2: Applying Coupon Code](#test-case-2-applying-coupon-code)
    - [Test Case 5: Changing Quantity in Cart](#test-case-5-changing-quantity-in-cart)
    - [Test Case 7: Applying Invalid Coupon Code](#test-case-7-applying-invalid-coupon-code)
    - [Test Case 9: Continue Shopping Button](#test-case-9-continue-shopping-button)
    - [Test Case 10: Save for Later](#test-case-10-save-for-later)
    - [Test Case 11: Edit Cart Items](#test-case-11-edit-cart-items)
    - [Test Case 12: Multiple Products in Cart](#test-case-12-multiple-products-in-cart)
4. [Preconditions](#preconditions)
5. [Steps](#steps)
6. [Expected Outcomes](#expected-outcomes)
7. [Notes](#notes)

## Introduction
This document provides detailed technical documentation for the automated tests conducted on the e-commerce shopping cart functionality using the Selenium framework.

## Test Environment Setup
- Browser: Google Chrome
- Web Driver: ChromeDriver
- Programming Language: Python
- Testing Framework: unittest
- Target E-commerce Website: https://www.amazon.com

## Test Case Descriptions

### Test Case 1: Adding Product to Cart
#### Preconditions
- The user is on the Amazon homepage.

#### Steps
1. Search for a product using the search bar.
2. Click on a product link from the search results.
3. Add the product to the cart.
4. Navigate to the cart page.

#### Expected Outcomes
- The product should be displayed in the cart with the correct details.

### Test Case 2: Applying Coupon Code
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Apply a coupon code to the cart.

#### Expected Outcomes
- The discounted price should be reflected in the subtotal.

### Test Case 5: Changing Quantity in Cart
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Change the quantity of the product.
3. Verify that the subtotal updates accordingly.

#### Expected Outcomes
- The subtotal should match the product price multiplied by the new quantity.

### Test Case 7: Applying Invalid Coupon Code
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Apply an invalid coupon code.

#### Expected Outcomes
- An appropriate error message should be displayed.

### Test Case 9: Continue Shopping Button
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Click the 'Continue Shopping' button.

#### Expected Outcomes
- The user should be redirected to the shopping page.

### Test Case 10: Save for Later
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Click on 'Save for later'.

#### Expected Outcomes
- The item should be moved to the 'Save for Later' list.

### Test Case 11: Edit Cart Items
#### Preconditions
- The user has added a product to the cart.

#### Steps
1. Navigate to the cart page.
2. Click on 'Edit' to change the quantity of the item.
3. Update the quantity.

#### Expected Outcomes
- The quantity of the item should be updated.

### Test Case 12: Multiple Products in Cart
#### Preconditions
- The user has added multiple products to the cart.

#### Steps
1. Add two different products to the cart.
2. Navigate to the cart page.

#### Expected Outcomes
- Both products should be displayed in the cart with correct details.

## Notes
- This documentation provides a comprehensive overview of the test cases for the e-commerce shopping cart functionality.
- Ensure that the test environment setup is accurately configured before running the tests.
- The expected outcomes mentioned in each test case are based on assumptions and expected behaviors.
- Test data and placeholder values need to be updated with actual data relevant to the testing environment.
- Always refer to the actual website's structure and elements while implementing and running the tests.

---
