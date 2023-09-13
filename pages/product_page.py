from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
 def add_bucket(self):
  link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET)
  link.click()
 def should_be_add_button(self):
  assert self.is_element_present(*ProductPageLocators.ADD_TO_BUCKET), "there is not add button"