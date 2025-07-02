from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Encontrar todos los elementos
elements = driver.find_elements(By.XPATH, ".//img")

# Comprobar que el número de elementos encontrados es mayor que 1 usando len()
assert len(elements) > 1, f"Expected more than 1 <img> element, but found {len(elements)}"

# Cerrar el navegador
driver.quit()