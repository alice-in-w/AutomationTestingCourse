import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обʼєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"/Users/apple/AutomationTestingCourse/" + "chromedriver")
    )

    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне імʼя користувача
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильну поштову адресу
    login_elem.send_keys("placeholder@email.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrongpass")

    # Знаходимо кнопку Sign In
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою миші
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()
