import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Crea una instancia limpia de Chrome para cada test
    y la cierra al finalizar.
    """

    options = Options()
    options.add_argument("--start-maximized")

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()