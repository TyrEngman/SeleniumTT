from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar el navegador
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la página
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(2)  # Espera para que los elementos se carguen

# Buscar el botón "Iniciar sesión" y hacer clic en él (todo en una sola línea)
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

# Esperar unos segundos para ver la acción (opcional)
time.sleep(2)

# Cerrar el navegador
driver.quit()
