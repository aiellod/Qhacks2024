################################################
# Contains all the functions for communicating #
# with WhatsApp Web using Selenium.            #
################################################

# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from localvars import WEBDRIVERPATH


#Setup global consants
chat_name = "Daniel" #replace wih the testing chat

# Create a new instance of the Edge driver
options = Options()
driver = webdriver.Edge(service=Service(WEBDRIVERPATH), options=options)


# Function to initialize the WhatsApp web client and reader
def init():
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code and log in
    input("Scan the QR code, then press Enter to continue...")
    
    #Add code to get most recent chat (similar to getting last message)

    # Enter defined chat rather than most recent to prevent 
    #   someone from accidentally ruining the demo
    chat_xpath = f'//span[@title="{chat_name}"]'
    chat_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, chat_xpath))
    )
    chat_element.click()
    input("Selected chat, press Enter to continue...")

# Function to get the last message from a specific chat
def get_last_message():
    # Make sure chat is loaded and get message
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-in')) #whatsapp recieved message class
    )

    # Get the last message in the chat as text
    messages = driver.find_elements(By.CLASS_NAME, 'message-in') #whatsapp recieved message class
    last_message = messages[-1].find_elements(By.CLASS_NAME, 'selectable-text')[-1].text

    return last_message

def send_message(message):
    # Find find the text field to type the message into
    text_field = driver.find_element(By.XPATH, '//*[@title="Type a message"]')

    # Type message
    text_field.send_keys(message)

    # Press Enter
    text_field.send_keys(Keys.ENTER)


# ---TESTING---
#Functions for testing
def test_recieve():
    last_message = get_last_message()
    print(f"Last message in '{chat_name}': {last_message}")

def test_send():
    message = "I'm a happy monkey living in a tree, get this and I'll be happy as can be!"
    send_message(message)
    print(f"Sent message: {message}")



# ----MAIN---- #
if __name__ == "__main__":
    # Initialize the WhatsApp web client
    init()

    # Put tests here
    test_send()

    # Ending cleanup
    input("Done, press Enter to close...")
    driver.quit()


