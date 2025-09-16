from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Iniciar sesión
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # El localizador de copy right
    footer = (By.CLASS_NAME, 'footer__copyright')
