import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrom_options
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose languages")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        options = chrom_options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("prefs", {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = firefox_option()
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        # options.profile = fp
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser
    browser.quit()
