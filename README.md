# Proyecto de Automatización QA - Walter Liendo

## Descripción

Proyecto de pre-entrega del curso de Automatización QA.

El objetivo es automatizar pruebas funcionales sobre el sitio SauceDemo utilizando Python, Selenium WebDriver y Pytest.

Se validan los siguientes flujos:

- Inicio de sesión con credenciales válidas.
- Visualización del catálogo de productos.
- Validación de elementos principales de la interfaz.
- Obtención del nombre y precio del primer producto.
- Agregado de un producto al carrito.
- Validación del contador del carrito.
- Verificación del producto dentro del carrito.

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Pytest HTML
- Git
- GitHub

## Sitio utilizado

https://www.saucedemo.com/

## Credenciales de prueba

Usuario:

```text
standard_user
```

Contraseña:

```text
secret_sauce
```

## Estructura del proyecto

```text
pre-entrega-automation-testing-walter-liendo/
│
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   └── helpers.py
│
├── reports/
│   └── reporte.html
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Walter185/pre-entrega-automation-testing-walter-liendo.git
```

Ingresar a la carpeta del proyecto:

```bash
cd pre-entrega-automation-testing-walter-liendo
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de los tests

Para ejecutar todos los tests:

```bash
python -m pytest -v
```

## Generación del reporte HTML

Para ejecutar las pruebas y generar el reporte:

```bash
python -m pytest -v --html=reports/reporte.html
```

El reporte generado se guarda en:

```text
reports/reporte.html
```

## Pruebas implementadas

### Login

Se valida:

- Ingreso con usuario y contraseña válidos.
- Redirección a `/inventory.html`.
- Visualización del título `Products`.

### Catálogo

Se valida:

- Visualización del título del catálogo.
- Existencia de productos.
- Nombre del primer producto.
- Precio del primer producto.
- Menú visible.
- Filtro de productos visible.

### Carrito

Se valida:

- Agregado del primer producto.
- Contador del carrito igual a `1`.
- Navegación al carrito.
- Presencia del producto agregado.

## Resultado de ejecución

Resultado actual:

```text
3 passed
```

Los tres casos de prueba se ejecutan correctamente.

## Autor

Walter Liendo
