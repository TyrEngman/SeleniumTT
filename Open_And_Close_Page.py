from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the test stand page
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Check that /signin was added to the URL
assert '/signin' in driver.current_url

# Close the browser
driver.quit()
