import pytest

def test_registration_button_text(driver):
    page = RegistrationPageAround(driver)
    # Validar el texto del botón
    assert page.button_text() == "Registrarse", "El texto del botón no es 'Registrarse'"

def test_can_click_registration_button(driver):
    page = RegistrationPageAround(driver)
    # Solo validamos que el clic no lance excepción (la navegación posterior depende de la app)
    page.click_register()
