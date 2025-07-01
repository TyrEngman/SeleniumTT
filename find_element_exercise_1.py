from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia el navegador
driver = webdriver.Chrome()
driver.maximize_window()

# Abre la página
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Espera hasta que aparezca el título del formulario
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".auth-form__title"))
)

# Opcional: obtener el texto del título
title = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")
print("Texto del título:", title.text)

# Cierra el navegador
driver.quit()
