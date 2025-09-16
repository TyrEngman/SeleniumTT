from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = Tuple[str, str]

class RegistrationPageAround:
    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # --- Localizadores requeridos ---
    registration_button: Locator = (By.CLASS_NAME, "auth-form__button")  # botón "Registrarse"

    # --- Métodos requeridos ---
    def click_register(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.registration_button)).click()

    def button_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.registration_button)).text
