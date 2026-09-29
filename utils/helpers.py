from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_LOGIN = "https://www.saucedemo.com/"


def login(driver):
    """
    Realiza el login en SauceDemo con credenciales válidas
    y espera a que se cargue la página de inventario.
    """

    driver.get(URL_LOGIN)

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    username.send_keys("standard_user")

    driver.find_element(
        By.NAME,
        "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.CSS_SELECTOR,
        'input[type="submit"]'
    ).click()

    wait.until(
        EC.url_contains("/inventory.html")
    )