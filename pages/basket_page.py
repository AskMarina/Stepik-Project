from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
			"Basket is not empty"

	def should_be_message_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.MS_BASKET_EMPTY), \
			"Empty basket message should be presented"
