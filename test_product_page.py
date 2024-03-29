from selenium import webdriver
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
 link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offerN"
 page = ProductPage(browser, link)
 page.open()
 page.should_be_add_button()
 page.add_bucket()
 page.solve_quiz_and_get_code()