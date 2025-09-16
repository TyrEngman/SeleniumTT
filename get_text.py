import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia el navegador
driver = webdriver.Chrome()

# Abre la página de inicio de sesión
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Pausa opcional para ver el navegador (solo visual, no recomendada en producción)
time.sleep(10)

# Llenar los campos de login
driver.find_element(By.ID, "email").send_keys("paragithub@tt.com")
driver.find_element(By.ID, "password").send_keys("todosquierenganar")

# Hacer clic en el botón "Iniciar sesión"
driver.find_element(By.XPATH, "//button[text()='Iniciar sesión']").click()

# Espera explícita a que la página principal se cargue completamente
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "header__user"))
)

# Encuentra el botón "Cerrar sesión" por clase y obtiene su texto
logout_button_text = driver.find_element(By.CLASS_NAME, "header__logout").text

# Verifica que el botón contiene el texto correcto
assert logout_button_text == "Cerrar sesión", f"Texto inesperado: {logout_button_text}"

# Cierra el navegador
driver.quit()
