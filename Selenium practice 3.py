from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

try:
    # Espera a que el campo email sea clickable (evita “no such element”)
    email = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    email.clear()
    email.send_keys("paragithub@tt.com")

    pwd = driver.find_element(By.ID, "password")
    pwd.clear()
    pwd.send_keys("todosquierenganar")

    driver.find_element(By.CLASS_NAME, "auth-form__button").click()

    # Espera a que cargue el feed
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "places__list"))
    )

    # Toma la primera tarjeta por CSS y desplázala a la vista
    first_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".places__item"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
        first_card
    )

    assert first_card.is_displayed()

finally:
    driver.quit()
