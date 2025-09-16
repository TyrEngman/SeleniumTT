import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://around-v1.nm.tripleten-services.com/signin?lng=es"

# ⚠️ Usa tus credenciales de prueba (las que estás usando en este curso)
EMAIL = "paragithub@tt.com"
PASSWORD = "todosquierenganar"

# Selectores y XPaths que usaremos varias veces
FIRST_TITLE_XPATH = "(//li[@class='places__item card']//h2[@class='card__title'])[1]"
ALL_CARDS_XPATH = "//li[@class='places__item card']"
ADD_BUTTON_CLASS = "profile__add-button"
PROFILE_USER_CLASS = "header__user"
MODAL_NEW_CARD_FORM_XPATH = ".//form[@name='new-card']/button[text()='Guardar']"
FIRST_CARD_DELETE_BUTTON_XPATH = "(//li[@class='places__item card'][1]//button[contains(@class,'card__delete-button')])[1]"

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1) Abrir e iniciar sesión
        driver.get(URL)

        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(EMAIL)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, "auth-form__button").click()

        # La página principal cargó (usuario visible)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, PROFILE_USER_CLASS)))

        # Asegurar que hay tarjetas visibles y tomar el título de la primera
        wait.until(EC.visibility_of_element_located((By.XPATH, FIRST_TITLE_XPATH)))
        title_before = driver.find_element(By.XPATH, FIRST_TITLE_XPATH).text

        # 2) Click en botón "Agregar"
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ADD_BUTTON_CLASS))).click()

        # 3) Nombre aleatorio y datos del modal
        new_title = f"Tokio{random.randint(100, 999)}"
        image_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg"

        wait.until(EC.visibility_of_element_located((By.NAME, "name"))).clear()
        driver.find_element(By.NAME, "name").send_keys(new_title)

        driver.find_element(By.NAME, "link").clear()
        driver.find_element(By.NAME, "link").send_keys(image_url)

        # 4) Guardar (botón del form new-card, por XPath)
        driver.find_element(By.XPATH, MODAL_NEW_CARD_FORM_XPATH).click()

        # 5) Esperar a que el título de la primera tarjeta contenga el new_title
        wait.until(EC.text_to_be_present_in_element((By.XPATH, FIRST_TITLE_XPATH), new_title))

        # 6) Afirmar que la primera tarjeta es exactamente el new_title
        first_title_after = driver.find_element(By.XPATH, FIRST_TITLE_XPATH).text
        assert first_title_after == new_title, f"Se esperaba '{new_title}' y se vio '{first_title_after}'"

        # 7) Esperar a que el botón de eliminar de la primera tarjeta esté presente y visible
        wait.until(EC.visibility_of_element_located((By.XPATH, FIRST_CARD_DELETE_BUTTON_XPATH)))

        # 8) Revertir el estado: eliminar la nueva tarjeta
        cards_before_delete = len(driver.find_elements(By.XPATH, ALL_CARDS_XPATH))
        driver.find_element(By.XPATH, FIRST_CARD_DELETE_BUTTON_XPATH).click()

        # 9) Esperar a que el primer título vuelva a mostrar el anterior (title_before)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, FIRST_TITLE_XPATH), title_before))

        # 10) Verificar que hay una tarjeta menos
        cards_after_delete = len(driver.find_elements(By.XPATH, ALL_CARDS_XPATH))
        assert cards_after_delete == cards_before_delete - 1, (
            f"Se esperaba {cards_before_delete - 1} tarjetas, pero hay {cards_after_delete}"
        )

        print("✅ Ejercicio 2 completado correctamente.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
