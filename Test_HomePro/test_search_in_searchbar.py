import pytest


@pytest.mark.regressiontest
def test_search_amazon(browser):
    browser.get("https://www.amazon.com/")
    search_bar = browser.find_element_by_id("twotabsearchtextbox").send_keys("Apple watch")
    search_bar.click()





