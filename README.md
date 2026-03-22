# Google Form Automation – Setup & Usage Guide

This document explains how to set up and run the Python automation script that fills and submits a Google Form 50 times, including file uploads to three separate “Add file” buttons.

---

## 📋 Prerequisites

- **Windows** operating system (the script uses absolute paths for Chrome and the file)
- **Python 3.7+** installed ([python.org](https://python.org))
- **Google Chrome** browser installed
- **The file to upload** (e.g., `calexterio_proof.jpg`) placed in your Downloads folder
- **Git** (optional, to clone the repository)

---

## 📦 Project Structure

```
google-form-automation/
│
├── main.py                  # The automation script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🛠️ Setup Instructions

### 1. Create a Project Folder and Virtual Environment

Open **PowerShell** or **Command Prompt** and run:

```powershell
# Create a new directory and navigate into it
mkdir google-form-automation
cd google-form-automation

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment (PowerShell)
.venv\Scripts\Activate.ps1
```

If you use Command Prompt, activate with:
```cmd
.venv\Scripts\activate.bat
```

You should see `(.venv)` appear at the beginning of the prompt.

### 2. Upgrade pip and install dependencies

First, upgrade pip to the latest version:
```powershell
python -m pip install --upgrade pip
```

Create a `requirements.txt` file with the following content:

```txt
selenium==4.15.2
webdriver-manager==4.0.1
pyautogui==0.9.54
```

Install all dependencies at once:
```powershell
pip install -r requirements.txt
```

Alternatively, you can install each package manually:
```powershell
pip install selenium webdriver-manager pyautogui
```

### 3. Save the Automation Script

Copy the final script (see the code block below) into a file named `main.py` inside your project folder.

---

## 🚀 Running the Automation

### Step 1: Start Chrome with Remote Debugging

1. **Close all Chrome windows** (this is essential to avoid profile conflicts).
2. Open a new **Command Prompt** window (not PowerShell) and run:

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug"
```

- If Chrome is installed in a different location, adjust the path accordingly.
- This launches a new Chrome window with a temporary profile.  
- **Important:** Leave this command prompt window open while the script runs.

3. In the new Chrome window, **log into your Google account** (`reymarkcalex@gmail.com` in this example).  
   - You can also navigate to the form URL if you want, but the script will do it later.

### Step 2: Run the Script

Go back to your project folder in **PowerShell** (where you activated the virtual environment) and execute:

```powershell
python main.py
```

The script will:

- Connect to the already running Chrome instance (via the debugging port).
- Automatically fill the text fields (email, full name, contact number, complete address).
- For each of the three “Add file” buttons:
  1. Click the button.
  2. Wait for the Google Picker iframe.
  3. Upload the file (using the hidden file input or pyautogui).
  4. Close the iframe.
- Submit the form.
- Click “Submit another response” (or refresh) and repeat for 50 submissions.

**Monitoring:** The terminal will display progress messages for each step. If an error occurs, a screenshot (`error_<submission#>.png`) is saved.

### Step 3: Stop the Script

The script will automatically close the browser after completing all 50 submissions. You can also stop it early by pressing **Ctrl+C** in the terminal.

---

## 📝 Requirements.txt

Create a file named `requirements.txt` with the following lines:

```
selenium>=4.15.0
webdriver-manager>=4.0.0
pyautogui>=0.9.54
```

This ensures the correct packages are installed.

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'selenium'` | Make sure your virtual environment is activated and dependencies are installed. |
| `WebDriverException: Message: unknown error: cannot find Chrome binary` | Chrome is not installed, or the path to Chrome in the remote‑debugging command is incorrect. |
| File upload fails or only the first button works | Ensure the script is using the final version with `close_picker_iframe()` called after each upload. Increase `time.sleep()` values if necessary. |
| Picker iframe stays open | The script attempts to close it using multiple methods. You can manually press `ESC` in the browser if it gets stuck. |
| Google sign-in page appears | The remote‑debugging Chrome window should already be logged in. If not, sign in manually within 60 seconds when the script waits. |

---

## 📜 Final Script (`main.py`)

```python
import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class GoogleFormAutomation:
    def __init__(self, debugger_address="localhost:9222"):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)

        self.form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeVlPbFB8O_VQlheU_cUKebQOwouv6JB2_d6FK2jP0wgty5DQ/viewform"

        self.form_data = {
            'email': 'reymarkcalex@gmail.com',
            'full_name': 'Reymark Calexterio',
            'contact_number': '09994956199',
            'complete_address': '53 Morato Avenue Damayan, Quezon City, Metro Manila, 1105'
        }

        self.file_path = "C:\\Users\\reyma\\Downloads\\calexterio_proof.jpg"
        if not os.path.exists(self.file_path):
            alt = "C:\\Users\\reyma\\Downloads\\calexterio_proof.JPG"
            if os.path.exists(alt):
                self.file_path = alt
        print(f"File exists: {os.path.exists(self.file_path)}")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def fill_text_fields(self):
        print("\n--- Filling text fields ---")
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="email"], input[type="tel"]')
        print(f"Found {len(inputs)} input fields")
        if len(inputs) >= 4:
            inputs[0].clear()
            inputs[0].send_keys(self.form_data['email'])
            print(f"✓ Email: {self.form_data['email']}")
            inputs[1].clear()
            inputs[1].send_keys(self.form_data['full_name'])
            print(f"✓ Full name: {self.form_data['full_name']}")
            inputs[2].clear()
            inputs[2].send_keys(self.form_data['contact_number'])
            print(f"✓ Contact: {self.form_data['contact_number']}")
            inputs[3].clear()
            inputs[3].send_keys(self.form_data['complete_address'])
            print(f"✓ Address: {self.form_data['complete_address']}")
            return True
        else:
            # Fallback by aria-label
            for field, value in self.form_data.items():
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, f'input[aria-label*="{field.replace("_", " ").title()}"]')
                    elem.clear()
                    elem.send_keys(value)
                    print(f"✓ {field} filled via aria-label")
                except:
                    pass
            return True

    def close_picker_iframe(self):
        """Force-close any Google Picker iframe."""
        self.driver.switch_to.default_content()
        try:
            iframes = self.driver.find_elements(By.CSS_SELECTOR, 'iframe[src*="docs.google.com/picker"]')
            if iframes:
                self.driver.switch_to.frame(iframes[0])
                try:
                    close_btn = self.driver.find_element(By.XPATH, "//div[@role='button' and contains(@aria-label, 'Close')]")
                    close_btn.click()
                    print("  Closed picker via close button")
                except:
                    pass
                self.driver.switch_to.default_content()
                pyautogui.press('esc')
                time.sleep(0.5)
                self.driver.execute_script("""
                    var iframes = document.querySelectorAll('iframe[src*="docs.google.com/picker"]');
                    iframes.forEach(iframe => iframe.remove());
                """)
                print("  Closed picker via JS removal")
                time.sleep(1)
        except:
            pass
        self.driver.switch_to.default_content()

    def upload_single_button(self, button, button_num):
        """Upload file for a single Add file button."""
        print(f"\n  Processing button {button_num}...")
        self.close_picker_iframe()
        time.sleep(0.5)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.5)

        button.click()
        print("  Clicked button, waiting for picker iframe...")
        time.sleep(2)

        try:
            picker_iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*="docs.google.com/picker"]'))
            )
            print("  Picker iframe found")
            self.driver.switch_to.frame(picker_iframe)
            time.sleep(1)

            try:
                file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(self.file_path)
                print("  Uploaded via file input")
            except:
                try:
                    browse_btn = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Browse')]")
                    browse_btn.click()
                    print("  Clicked Browse button")
                    time.sleep(1)
                    pyautogui.write(self.file_path)
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    print("  Uploaded via pyautogui")
                except:
                    print("  Could not find upload method")
                    raise

            self.driver.switch_to.default_content()
            time.sleep(3)
            self.close_picker_iframe()
            time.sleep(1)
            return True

        except Exception as e:
            print(f"  ✗ Error: {e}")
            self.driver.switch_to.default_content()
            self.close_picker_iframe()
            return False

    def upload_files(self):
        print("\n--- Uploading files to all three buttons ---")
        add_buttons = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Add file')]")
        if not add_buttons:
            add_buttons = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Add file')]")
        if not add_buttons:
            print("✗ No 'Add file' buttons found")
            return False

        print(f"Found {len(add_buttons)} 'Add file' button(s)")
        success = 0
        for i, btn in enumerate(add_buttons[:3], 1):
            if self.upload_single_button(btn, i):
                success += 1
            else:
                print(f"  Failed on button {i}")

        print(f"Uploaded to {success} file field(s)")
        return success > 0

    def submit_form(self):
        print("\n--- Submitting form ---")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            submit = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]/..")
            submit.click()
            print("✓ Form submitted")
            return True
        except:
            print("✗ Submit button not found")
            return False

    def submit_another(self):
        print("\n--- Submitting another response ---")
        time.sleep(3)
        try:
            link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Submit another response')]")
            link.click()
            print("✓ Clicked 'Submit another response'")
            time.sleep(2)
            return True
        except:
            print("⚠ Link not found, refreshing form...")
            self.driver.get(self.form_url)
            time.sleep(3)
            return True

    def run_submission(self, sub_num):
        print(f"\n{'='*50}")
        print(f"Submission #{sub_num}")
        print(f"{'='*50}")
        self.fill_text_fields()
        self.upload_files()
        if self.submit_form():
            if sub_num < 50:
                self.submit_another()
            return True
        return False

    def run_all(self, total=50):
        if "viewform" not in self.driver.current_url:
            self.driver.get(self.form_url)
            time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        time.sleep(2)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="email"], input[type="tel"]')
        print(f"\nForm ready. Found {len(inputs)} text fields.")

        successful = 0
        start = time.time()
        for i in range(1, total + 1):
            try:
                if self.run_submission(i):
                    successful += 1
                else:
                    print(f"❌ Submission {i} failed")
                if i < total:
                    delay = 5
                    print(f"\nWaiting {delay} seconds...")
                    time.sleep(delay)
            except KeyboardInterrupt:
                print("\nStopped by user")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.driver.save_screenshot(f"error_{i}.png")
                time.sleep(5)

        elapsed = time.time() - start
        print(f"\n{'='*50}")
        print(f"COMPLETE: {successful}/{total} successful")
        print(f"Time: {elapsed:.1f} seconds")
        input("Press Enter to close the browser...")
        self.driver.quit()

def main():
    print("=" * 60)
    print("INSTRUCTIONS:")
    print("1. Close all Chrome windows.")
    print("2. Start Chrome with remote debugging:")
    print('   "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\\temp\\chrome_debug"')
    print("3. In that Chrome window, log into your Google account (reymarkcalex@gmail.com).")
    print("4. Optionally, navigate to the form URL (or let the script do it).")
    print("5. Run this script.")
    print("=" * 60)
    input("Press Enter after Chrome is running and you're logged in...")

    bot = GoogleFormAutomation()
    try:
        bot.run_all(50)
    except Exception as e:
        print(f"Fatal: {e}")
    finally:
        try:
            bot.driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()
```

---