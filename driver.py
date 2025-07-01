from selenium import webdriver


driver = webdriver.Chrome() # Google Chrome
# driver = webdriver.Firefox()  Firefox
# driver = webdriver.Ie()  Internet Explorer

chrome_options = webdriver.ChromeOptions() # Crea un objeto para la configuración
chrome_options.add_argument('--headless') # Ejecuta el navegador desde la terminal sin una interfaz gráfica
chrome_options.add_argument('--window-size=640,480') # Ajusta el tamaño de la ventana a 640 x 480 pixeles
driver = webdriver.Chrome(options=chrome_options) # Crea un controlador y pasa la configuración de los ajustes establecidos