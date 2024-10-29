# WhatsApp Bulk Image Messaging Script

This Python script allows users to **send images with a caption** to multiple phone numbers via WhatsApp Web. It utilizes the `pywhatkit` library for basic WhatsApp automation and `selenium` to interact with the WhatsApp Web interface for sending customized messages and images.

---

## Prerequisites

Before running the script, ensure the following:

### 1. **Python Libraries Installation**
The following libraries are required:
- `pywhatkit`
- `selenium`
- `webdriver-manager`
- `pyautogui`

Install them using:
```bash
pip install pywhatkit selenium webdriver-manager pyautogui
```

### 2. **Google Chrome and ChromeDriver Setup**
- **Google Chrome** must be installed on your machine.
- **ChromeDriver** must match the version of your Chrome browser. The `webdriver-manager` package will handle the installation automatically.
- Ensure that your **WhatsApp Web account** is linked to the Chrome profile you will use.

### 3. **User Data Path Setup**
- Update the Chrome **user data path** and **profile path** inside the script:
  ```python
  options.add_argument("--user-data-dir=C:/Users/A/AppData/Local/Google/Chrome/User Data")
  options.add_argument("C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
  ```
  Replace the paths with your **user’s actual data directory** to ensure WhatsApp Web opens with the correct account already logged in.

---

## Script Overview

This script is structured as follows:

### 1. **Variables Setup**
- **Phone Numbers List**  
   A list of phone numbers (with the country code) must be added:
   ```python
   phone_numbers = ["+911234567890", "+919876543210"]
   ```

- **Message with Caption**  
   You can customize the message caption under the `message` variable.

- **Image Path**  
   Update the image path to point to the desired image:
   ```python
   image_path = "WE’RE OFFERING INTERNSHIP (1).png"
   ```

### 2. **send_image_with_caption() Function**
This function:
1. Uses `pywhatkit` to open WhatsApp Web with the specified phone number.
2. Waits for 10 seconds to ensure the initial image is sent.
3. Uses Selenium to:
   - Open WhatsApp Web with the given Chrome profile.
   - Search for the contact by phone number.
   - Upload the image with a caption.
   - Send the message and image.

### 3. **send_bulk_messages() Function**
This function loops through a list of phone numbers and sends the image + caption to each. It also:
- **Closes each chat window** using `pyautogui` to press `ALT + F4` after sending each message to avoid errors.
- Sleeps for 5 seconds between messages to **prevent anti-spam measures**.

---

## How to Use

1. **Update Variables:**  
   Fill in the `phone_numbers`, `message`, and `image_path` in the script.

2. **Run the Script:**
   ```bash
   python whatsapp_bulk_sender.py
   ```

3. **Scan the QR Code (if needed):**  
   If the Chrome profile isn’t already logged into WhatsApp Web, scan the QR code manually.

---

## Example

If the phone numbers list contains:
```python
phone_numbers = ["+911234567890", "+919876543210"]
```
The script will:
1. Open WhatsApp Web for each contact.
2. Send the image along with the caption provided in the `message` variable.
3. Close the chat window after sending the message.

---

## Troubleshooting

1. **WebDriver Errors:**  
   Ensure that your Chrome version matches the **ChromeDriver** version. Try updating the ChromeDriver with:
   ```bash
   pip install --upgrade webdriver-manager
   ```

2. **WhatsApp Not Loading:**  
   Check if the **Chrome profile path** is correct and logged in to WhatsApp Web.

3. **Anti-Spam Issues:**  
   WhatsApp has spam-detection mechanisms. To avoid getting blocked:
   - Add **delays** between messages (already handled by `time.sleep()` in the script).
   - Avoid sending too many messages in quick succession.

---

## Dependencies

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Google Chrome**: Required for Selenium automation.
- **ChromeDriver**: Must be compatible with the installed Chrome version.

---

## License

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

---

## Disclaimer

This script is intended for educational purposes. Be mindful of **WhatsApp’s policies** when sending bulk messages to avoid being flagged as spam or having your number blocked.
