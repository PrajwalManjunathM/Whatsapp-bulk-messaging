import pywhatkit as kit
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

# List of phone numbers (include country code)
phone_numbers = [ ]

# Updated message to be sent as a caption
message = (
    "_\"We at Winger IT Solutions [Affiliated with AICTE-India] are thrilled to announce our internship programs,designed just for you.\"_\n\n"

    "_*Why Choose Our Internship Program?*_\n"

    "✅ *Hands-on Experience:* Work on real-time projects and gain practical knowledge.\n"
    "✅ *Skill Development:* Enhance your technical, communication, and teamwork skills.\n"
    "✅ *Industry Exposure:* Experience a corporate environment and prepare for professional challenges.\n"
    "✅ *Support:* Receive comprehensive support throughout the program and ongoing assistance even after your internship ends.\n"
    "✅ *Expert Guidance:* Learn from industry experts and dedicated mentors.\n\n"

    "_*Got Questions?*_\n"
    "Feel free to reach out to us\n\n"

    "📞 +91 9035261715\n"
    "🌐 www.wingerit.in\n"
    "📍669, 2nd Block, 9th Main, 80 Feet Road, Near-BDA Complex, H B R Layout, Bangalore, Karnataka 560043.\n\n"

    "Looking forward to seeing you onboard!\n\n"

    "Best Regards,\n"
    "Winger IT Solutions Team")

# Path to the image file
image_path = "WE’RE OFFERING INTERNSHIP (1).png"


# Function to send image with caption
def send_image_with_caption(phone_number, message, image_path):
    # Open WhatsApp Web and wait for the QR code to be scanned
    kit.sendwhats_image(phone_number, image_path, message)
    time.sleep(10)  # Wait for the image to be sent

    # Initialize the WebDriver with user data path (Ensure ChromeDriver is in your PATH or specify the path)
      # Use your actual profile directory, e.g., 'Profile 1', 'Profile 2'
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:/Users/A/AppData/Local/Google/Chrome/User Data")  # Use your actual user data path
    options.add_argument("C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

    try:

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open WhatsApp Web
        driver.get('https://web.whatsapp.com')

        # Wait for WhatsApp Web to load
        time.sleep(15)

        # Find the chat by phone number and open it
        search_box = driver.find_element(By.XPATH, '//*[@title="Search or start new chat"]')
        search_box.click()
        search_box.send_keys(phone_number)
        time.sleep(2)

        user = driver.find_element(By.XPATH, f'//span[@title="{phone_number}"]')
        user.click()

        # Send the message as a caption with the image
        attachment_box = driver.find_element(By.XPATH, '//*[@title="Attach"]')
        attachment_box.click()

        image_box = driver.find_element(By.XPATH, '//*[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(image_path)

        time.sleep(10)  # Wait for the image to load

        caption_box = driver.find_element(By.XPATH, '//*[@class="_13NKt copyable-text selectable-text"]')
        caption_box.click()
        caption_box.send_keys(message)

        time.sleep(5)

        send_button = driver.find_element(By.XPATH, '//*[@data-icon="send"]')
        send_button.click()

        time.sleep(5)  # Wait for the message to be sent


    except Exception as e:
        print(f"An error occurred: {e}")

    # Function to send image with caption to a list of phone numbers
def send_bulk_messages(numbers, msg, img_path):
    for number in numbers:
        send_image_with_caption(number, msg, img_path)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(5)  # Sleep to avoid triggering anti-spam measures


# Call the function
send_bulk_messages(phone_numbers, message, image_path)







