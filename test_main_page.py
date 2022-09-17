import pytest
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    # 1 способ перейти на другую страницу
    # выполняем метод страницы - переходим на страницу логина (добавили return c объектом класса LoginPage и передали в переменную)
    # login_page = page.go_to_login_page()  # добавили ретурн в метод go_to_login_page который теперь возвращает объект класса LoginPage c текущим браузером и текущей url на страницу с login
    # login_page.should_be_login_page() # спользуем метод из класса LoginPage, для проверки страницы login_page
    #page.should_be_login_link()  # проверяем есть ли кнопка на логин

    # 2 способ перехода на страницу login_page
    # убираем return в методе go_to_login_page в классе MainPage, реализуем этот метод с объектом page
    page.go_to_login_page()
    # инициалтзируем новый объект класса LoginPage
    login_page = LoginPage(browser, browser.current_url)
    # применяем метод из класса LoginPage для объекта LoginPage
    login_page.should_be_login_page()



# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     time.sleep(15)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

#
#
# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR,"#login_link")
#     login_link.click()
#
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)

# pytest -v --tb=line --language=en test_main_page.py