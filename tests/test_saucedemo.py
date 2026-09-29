from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_catalogo(driver):
    """
    Verifica que el catálogo cargue correctamente,
    que existan productos visibles y que los elementos
    principales de la interfaz estén presentes.
    """

    login(driver)

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()

    print("Primer producto:", nombre)
    print("Precio:", precio)
    print("Test OK - Catálogo validado")

def test_carrito(driver):
    """
    Verifica que se pueda agregar el primer producto al carrito
    y que el producto aparezca correctamente dentro del mismo.
    """

    login(driver)

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    boton_agregar = primer_producto.find_element(
        By.TAG_NAME,
        "button"
    )

    boton_agregar.click()

    wait = WebDriverWait(driver, 10)

    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "1"

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre_producto

    print("Test OK - Producto agregado al carrito")