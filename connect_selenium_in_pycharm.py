from selenium import webdriver
import time
#inicializa el controlador
driver = webdriver.Chrome()

#Agregar una espera
time.sleep(5)

#Cerrar el navegador
driver.quit()