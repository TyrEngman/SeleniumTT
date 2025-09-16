from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("paragithub@tt.com")
driver.find_element(By.ID, "password").send_keys("todosquierenganar")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Esperar a que cargue una imagen para confirmar que entramos a la página principal
WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image"))
)

# Esperar unos segundos más para que se cargue todo
time.sleep(2)

# Buscar el pie de página usando la etiqueta <footer>
footer_element = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", footer_element)

# Verificar que contiene el texto 'Around'
assert 'Around' in footer_element.text

# Cerrar el navegador
driver.quit()
