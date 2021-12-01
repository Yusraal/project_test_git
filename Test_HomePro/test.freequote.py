import pytest


def test_freequote(browser):
    browser.get("https://homepro.herokuapp.com/quote.php")
    first_name = browser.find_element_by_name("first_name").send_keys("Ahmad")
