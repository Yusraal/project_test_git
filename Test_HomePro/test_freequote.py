import time

import pytest

@pytest.mark.smoketest
def test_freequote(browser):
    browser.get("https://homepro.herokuapp.com/quote.php")
    assert browser.title == "HomePro, Inc"
    print(browser.title)
    first_name = browser.find_element_by_name("first_name").send_keys("Ahmad")
    time.sleep(3)
