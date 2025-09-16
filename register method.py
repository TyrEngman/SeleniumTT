from selenium.webdriver.common.by import By

class RegistrationPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Registrarse
    registration_button = (By.CLASS_NAME, 'auth-form__button')

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # El método rellena el campo Correo electrónico
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    # El método rellena el campo Contraseña
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    # El método hace clic en el botón Registrarse
    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    # El método de registro combina el correo electrónico, la contraseña y el clic del botón
    def register(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_registration_button()