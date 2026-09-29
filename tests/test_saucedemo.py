from selenium.webdriver.common.by import By

from utils.helpers import login


def test_login_exitoso(driver):
    """
    Verifica que un usuario válido pueda iniciar sesión
    y acceder correctamente al inventario.
    """

    login(driver)

    assert "/inventory.html" in driver.current_url

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"

    print("Test OK - Login exitoso")