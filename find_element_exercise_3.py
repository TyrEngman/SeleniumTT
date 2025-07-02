from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la página en español
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(3)  # Espera para que los elementos estén disponibles

# Buscar los campos por su ID
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Verificar los placeholders en español
assert email.get_attribute("placeholder") == "Correo electrónico", "❌ El placeholder del campo 'email' es incorrecto"
assert password.get_attribute("placeholder") == "Contraseña", "❌ El placeholder del campo 'contraseña' es incorrecto"
print("Pruebas exitosas!")

# Cerrar el navegador
driver.quit()
