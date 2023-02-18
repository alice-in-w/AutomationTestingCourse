from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.usefixtures
def test_check_incorrect_username_page_object():
    # Створюємо обʼєкт сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("randomemail@gmail.com", "randompassword")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()
