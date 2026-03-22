```markdown
# Google Form Automation – Upload Files & Submit 50 Times

This Python script automates filling and submitting a Google Form 50 times. It fills text fields (email, full name, contact number, complete address) and uploads the **same file** to **three separate "Add file" buttons** on the form. After each submission, it automatically clicks "Submit another response" and repeats.

Perfect for when you need to submit many responses without manual work.

## 📦 Project Structure

```
google-form-automation/
│
├── main.py                  # The automation script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🚀 How It Works

1. The script connects to a Chrome browser you start **manually** (using remote debugging).  
2. You log into your Google account **once** in that browser.  
3. The script fills the form, clicks each "Add file" button, uploads the file (via pyautogui), and submits.  
4. It repeats 50 times, waiting a few seconds between submissions.

---

## 📋 Prerequisites

- **Windows** (the script uses absolute paths for Chrome and the file).
- **Python 3.7 or higher** installed.
- **Google Chrome** installed.
- A file to upload (e.g., `calexterio_proof.jpg`) placed in your Downloads folder.
- A GitHub account (if you plan to clone the repo). Not required to run the script.

---

## 🛠️ Setup Instructions 

### 1. Install Python (if you don't have it)
- Go to [python.org/downloads](https://www.python.org/downloads/)
- Download the latest Python for Windows.
- **During installation, check the box "Add Python to PATH"**.
- Open a new Command Prompt and type `python --version` to verify.

### 2. Create a Project Folder
Open **File Explorer**, create a new folder, e.g., `C:\Users\YourName\google-form-automation`.

### 3. Download the Script
- Copy the `main.py` script from this repository into your folder.
- Create a file named `requirements.txt` with these lines:
  ```
  selenium>=4.15.0
  webdriver-manager>=4.0.0
  pyautogui>=0.9.54
  ```

### 4. Open PowerShell in the Project Folder
- In File Explorer, navigate to your folder.
- Click **File** → **Open Windows PowerShell** (or hold **Shift** + right-click and choose **Open PowerShell window here**).

### 5. Create a Virtual Environment
Run these commands one by one:

```powershell
# Create the virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

If you see an error about execution policy, run this once and then try again:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

After activation, you should see `(.venv)` at the beginning of the prompt.

### 6. Install Required Packages
```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install everything from requirements.txt
pip install -r requirements.txt
```

### 7. **Customize the Script** (Very Important!)
Open `main.py` in a text editor (like Notepad). You need to change a few lines to match your own information.

#### A. Change the file to upload
Look for this line near the top:
```python
self.file_path = "C:\\Users\\reyma\\Downloads\\calexterio_proof.jpg"
```
Replace the path with the full path to **your** file. For example:
- If your file is `my_picture.png` in `C:\Users\John\Downloads`, change it to:
  ```python
  self.file_path = "C:\\Users\\John\\Downloads\\my_picture.png"
  ```
- If you are not sure of the path, you can open File Explorer, navigate to the file, click the address bar, and copy the full path. Then paste it inside the quotes, making sure to use **double backslashes** (`\\`).

#### B. Change the email address
Look for:
```python
self.form_data = {
    'email': 'reymarkcalex@gmail.com',
    'full_name': 'Reymark Calexterio',
    'contact_number': '09994956199',
    'complete_address': '53 Morato Avenue Damayan, Quezon City, Metro Manila, 1105'
}
```
Change the `'email'` value to your own email (the one you will use to log into Google and that should appear in the form). For example:
```python
'email': 'yourname@gmail.com',
```

#### C. Change the other fields (optional)
If the form expects different text, change the values for `full_name`, `contact_number`, and `complete_address` as needed.

#### D. Save the file (Ctrl+S)

### 8. Place Your File in the Location You Specified
Make sure the file exists exactly at the path you wrote in step 7A. For example, if you set `C:\\Users\\YourName\\Downloads\\my_picture.png`, that file must be there.

### 9. Start Chrome with Remote Debugging
**Close all Chrome windows** first! Then open a **new Command Prompt** (not PowerShell) and run:

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug"
```

If Chrome is installed elsewhere, adjust the path.

- A new Chrome window will open. **Log into your Google account** (the same email you set in step 7B).
- You can also navigate to the form URL if you want, but the script will do that later.
- **Keep this Command Prompt window open** – the script will connect to this Chrome instance.

### 10. Run the Script
Go back to the PowerShell window (where your virtual environment is active) and run:

```powershell
python main.py
```

The script will:
- Connect to the already open Chrome window.
- Fill the text fields.
- For each of the three "Add file" buttons, click it, upload the file, and close the file picker.
- Submit the form.
- Click "Submit another response" (or refresh if not found).
- Repeat for 50 submissions.

You'll see progress messages in the terminal. If anything goes wrong, a screenshot (`error_1.png`, `error_2.png`, …) will be saved in the project folder.

### 11. Stop the Script
- Press **Ctrl+C** in the PowerShell window to stop early.
- The script will automatically close the browser after finishing all 50 submissions.

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'selenium'` | You forgot to activate the virtual environment. Run `.venv\Scripts\Activate.ps1` first. |
| Chrome doesn't open with remote debugging | Make sure you closed all Chrome windows first. The command may fail if another Chrome instance is running. |
| `WebDriverException: unknown error: cannot find Chrome binary` | Your Chrome is not installed in the default location. Find the path and update the command in step 9. |
| File not found error | Double‑check the file path in the script (step 7A). The file must exist exactly there. |
| Only the first "Add file" button works | The script now properly closes the file picker after each upload. If it still fails, try increasing the `time.sleep()` values in the script. |
| The script cannot find the "Add file" button | Google Forms sometimes loads slowly. Try increasing the initial `time.sleep()` after loading the form. |
| Google sign-in page appears | You didn't log in during step 9. Log in in the Chrome window before running the script. |
| pyautogui types the file path but it doesn't upload | Ensure the file dialog is the active window. Do not move the mouse or type during the upload. |

---

## 📄 Files in This Repository

- `main.py` – The automation script.
- `requirements.txt` – Python dependencies.
- `README.md` – This file.

---

## 📝 Customization

### Change the number of submissions
In `main.py`, near the end, find:
```python
bot.run_all(50)
```
Change the `50` to any number you want (e.g., `100`).

### Change the text fields
Edit the `self.form_data` dictionary in the `__init__` method. For example:
```python
self.form_data = {
    'email': 'your-email@example.com',
    'full_name': 'Jane Doe',
    'contact_number': '1234567890',
    'complete_address': '123 Main St, City, Country'
}
```

### Change the file to upload
Edit the line `self.file_path = ...` as explained in step 7A.

---

## 📜 License

This project is open‑source under the MIT License. Feel free to use, modify, and share it.

---

## 🙌 Credits

Built with Python, Selenium, and pyautogui.  
If you have any questions, open an issue on GitHub or contact the repository owner.

---

**Happy automating!** 🚀