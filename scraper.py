from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

project_path = os.path.dirname(os.path.abspath(__file__))
print(project_path)

# Set up the WebDriver (make sure to provide the correct path to your webdriver)
options = Options()
executable_path = project_path + '\\msedgedriver.exe'

# Create a new instance of the Edge driver
driver = webdriver.Edge(service=Service(executable_path), options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and log in
input("Scan the QR code, then press Enter to continue...")

# Function to get the last message from a specific chat
def get_last_message(chat_name):
    chat_xpath = f'//span[@title="{chat_name}"]'
    chat_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, chat_xpath))
    )
    chat_element.click()
    input("Selected chat, press Enter to continue...")
    # Wait for the chat to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-in'))
    )

    # Get the last message
    messages = driver.find_elements(By.CLASS_NAME, 'message-in')
    last_message = messages[-1].find_elements(By.CLASS_NAME, 'selectable-text')[-1].text

    return last_message

# Example usage
chat_name = "Daniel"  # Replace with the name of the chat you want to retrieve messages from
last_message = get_last_message(chat_name)
print(f"Last message in '{chat_name}': {last_message}")

input("Done, press Enter to close...")
# Close the browser

driver.quit()

