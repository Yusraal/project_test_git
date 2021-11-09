import pytest
@pytest.mark.smoketest
def test_basic_navigation_amazon(browser):

    browser.get("https://www.amazon.com/")
