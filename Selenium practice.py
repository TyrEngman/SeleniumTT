# practice_exercise_1.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://around-v1.nm.tripleten-services.com/signin?lng=es"
EMAIL = "paragithub@tt.com"
PASSWORD = "todosquierenganar"
NEW_AVATAR = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"

def main():
    # Arranca Chrome con WebDriverManager (evita problemas de versión)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # 1) Ir al login
        driver.get(URL)

        # 2) Login (esperas explícitas)
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(EMAIL)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, "auth-form__button").click()

        # 3) Espera a que cargue la página principal (ya logueado)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".profile__image")))

        # 4) Clic en la foto de perfil
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".profile__image"))).click()

        # 5) Espera a que aparezca el formulario del modal y escribe la URL del avatar
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[name="edit-avatar"]')))
        inp = wait.until(EC.element_to_be_clickable((By.ID, "owner-avatar")))
        inp.clear()
        inp.send_keys(NEW_AVATAR)

        # 6) Clic en el botón Guardar (independiente del idioma)
        save_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//form[@name="edit-avatar"]//button[@type="submit"]'))
        )
        save_btn.click()

        # 7) Espera a que el 'style' de la foto contenga la nueva URL
        wait.until(
            lambda d: NEW_AVATAR in d.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute("style")
        )
        style_value = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute("style")
        assert NEW_AVATAR in style_value, f"No se actualizó el avatar. style: {style_value}"
        print("✅ Avatar actualizado correctamente.")

        # 8) Assert final del atributo style
        style_value = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute("style")
        assert NEW_AVATAR in style_value, f"No se actualizó el avatar. style: {style_value}"
        print("✅ Avatar actualizado correctamente.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
