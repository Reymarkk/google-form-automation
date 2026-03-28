import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

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
        # Try to find the iframe
        try:
            iframes = self.driver.find_elements(By.CSS_SELECTOR, 'iframe[src*="docs.google.com/picker"]')
            if iframes:
                # First try to click the close button inside iframe
                self.driver.switch_to.frame(iframes[0])
                try:
                    close_btn = self.driver.find_element(By.XPATH, "//div[@role='button' and contains(@aria-label, 'Close')]")
                    close_btn.click()
                    print("  Closed picker via close button")
                except:
                    pass
                self.driver.switch_to.default_content()
                # If still there, try ESC key
                pyautogui.press('esc')
                time.sleep(0.5)
                # Finally, remove the iframe via JavaScript if still present
                self.driver.execute_script("""
                    var iframes = document.querySelectorAll('iframe[src*="docs.google.com/picker"]');
                    iframes.forEach(iframe => iframe.remove());
                """)
                print("  Closed picker via JS removal")
                time.sleep(1)
        except:
            pass
        self.driver.switch_to.default_content()

    def upload_single_button(self, button, button_num, retry_count=0):
        """Upload file for a single Add file button."""
        print(f"\n  Processing button {button_num}...")
        # Ensure no leftover iframe
        self.close_picker_iframe()
        time.sleep(0.5)

        # Scroll to button
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.5)

        # Click the button
        button.click()
        print("  Clicked button, waiting for picker iframe...")
        time.sleep(2)

        # Wait for picker iframe to appear
        try:
            picker_iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*="docs.google.com/picker"]'))
            )
            print("  Picker iframe found")
            self.driver.switch_to.frame(picker_iframe)
            time.sleep(1)

            # Check if the picker is blank (no upload controls)
            try:
                # Try to find either file input or browse button within a short timeout
                WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"], div[contains(text(), "Browse")]'))
                )
            except TimeoutException:
                # Blank dialog detected
                print("  Blank picker detected (no upload controls) – closing and refreshing")
                self.driver.switch_to.default_content()
                self.close_picker_iframe()
                # Refresh the page to reset
                self.driver.refresh()
                time.sleep(2)
                # Re-fill text fields (since refresh cleared them)
                self.fill_text_fields()
                # Re-find the button (it's now stale) and retry upload for this button
                # Re-fetch all add file buttons
                add_buttons = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Add file')]")
                if not add_buttons:
                    add_buttons = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Add file')]")
                if len(add_buttons) >= button_num:
                    new_button = add_buttons[button_num-1]
                    if retry_count < 2:  # prevent infinite loops
                        return self.upload_single_button(new_button, button_num, retry_count+1)
                    else:
                        print(f"  Max retries reached, giving up on button {button_num}")
                        return False
                else:
                    print(f"  Could not re-find button {button_num} after refresh")
                    return False

            # Normal upload flow (picker has controls)
            # Look for file input or browse button
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

            # Switch back to default content
            self.driver.switch_to.default_content()
            time.sleep(3)  # Wait for upload to start

            # Close the picker iframe
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
        # Find all "Add file" buttons
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
        # Ensure we're on the form page
        if "viewform" not in self.driver.current_url:
            self.driver.get(self.form_url)
            time.sleep(3)
        # Wait for form to load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        time.sleep(2)
        # Debug
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