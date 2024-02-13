import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def can_add_product_to_basket(self):
		self.should_add_product_to_basket()
		self.should_be_same_name()
		time.sleep(3)

	def should_add_product_to_basket(self):
		basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
		basket_link.click()
		BasePage.solve_quiz_and_get_code(self)

	def should_be_same_name(self):
		assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
			*ProductPageLocators.MS_PRODUCT_NAME).text, 'The product name in the message does not match the added product'

	def should_be_same_price(self):
		assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
			*ProductPageLocators.MS_PRODUCT_PRICE).text, 'The cost of the basket does not match the price of the product'
