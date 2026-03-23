
# 🚀 Google Form Automation – Bulk Submission with File Upload

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://python.org)
[![Selenium](https://img.shields.io/badge/selenium-4.15%2B-brightgreen)](https://selenium.dev)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Automate filling and submitting a Google Form **50 times** (configurable) with text fields and file uploads to **three separate “Add file” buttons**. Perfect for repetitive form submissions.

---

## 📖 Table of Contents

- [How It Works](#-how-it-works)
- [Prerequisites](#-prerequisites)
- [Setup Instructions (Step‑by‑Step)](#-setup-instructions-step‑by‑step)
  - [1. Install Python](#1-install-python)
  - [2. Create a Project Folder](#2-create-a-project-folder)
  - [3. Download the Script & Requirements](#3-download-the-script--requirements)
  - [4. Open PowerShell in the Folder](#4-open-powershell-in-the-folder)
  - [5. Create & Activate a Virtual Environment](#5-create--activate-a-virtual-environment)
  - [6. Install Dependencies](#6-install-dependencies)
  - [7. **Customize the Script** (Crucial!)](#7-customize-the-script-crucial)
  - [8. Place Your File in the Right Location](#8-place-your-file-in-the-right-location)
  - [9. Start Chrome with Remote Debugging](#9-start-chrome-with-remote-debugging)
  - [10. Run the Script](#10-run-the-script)
  - [11. Stop the Script](#11-stop-the-script)
- [Troubleshooting](#-troubleshooting)
- [Customization](#-customization)
- [Files in This Repository](#-files-in-this-repository)
- [License](#-license)
- [Credits](#-credits)

---

## ⚙️ How It Works

1. You manually start Chrome with remote debugging enabled (once).  
2. You log into your Google account **once** in that browser.  
3. The Python script connects to that browser and:
   - Fills the text fields: email, full name, contact number, complete address.
   - For each of the three “Add file” buttons:
     - Clicks the button.
     - Uploads your file using `pyautogui` (types the path and presses Enter).
     - Closes the file‑picker iframe.
   - Submits the form.
   - Clicks “Submit another response” (or refreshes if not found).
4. The loop repeats for the desired number of submissions (default 50).

---

## 📌 Prerequisites

- **Windows** (the script uses absolute paths for Chrome and the file)
- **Python 3.7+** ([download](https://www.python.org/downloads/))
- **Google Chrome** (latest version)
- A file to upload (e.g., `calexterio_proof.jpg`) placed somewhere accessible
- A GitHub account (optional, only if cloning the repo)

---

## 🛠️ Setup Instructions (Step‑by‑Step)

### 1. Install Python

- Download Python from [python.org](https://www.python.org/downloads/).
- During installation, **check “Add Python to PATH”**.
- Open a Command Prompt and verify:
  ```cmd
  python --version
  ```

### 2. Create a Project Folder

Create a folder where you’ll keep the script, e.g.:

```
C:\Users\YourName\google-form-automation
```

### 3. Download the Script & Requirements

- Copy the `main.py` script (from this repository) into your folder.
- Create a file named `requirements.txt` and paste:

```txt
selenium>=4.15.0
webdriver-manager>=4.0.0
pyautogui>=0.9.54
```

### 4. Open PowerShell in the Folder

- In File Explorer, navigate to your project folder.
- Click **File** → **Open Windows PowerShell** (or **Shift** + right‑click → **Open PowerShell window here**).

### 5. Create & Activate a Virtual Environment

Run these commands:

```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

If you get an execution policy error, run this once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

After activation, you should see `(.venv)` at the prompt.

### 6. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 7. **Customize the Script** (Crucial!)

Open `main.py` in a text editor (Notepad, VS Code, etc.). You **must** change the following lines.

#### ✏️ File to Upload

Find this line:

```python
self.file_path = "C:\\Users\\reyma\\Downloads\\calexterio_proof.jpg"
```

Replace it with the **full path** to your file.  
Example:

```python
self.file_path = "C:\\Users\\YourName\\Downloads\\my_image.png"
```

> **Note:** Use **double backslashes** (`\\`) in the path.

#### ✏️ Form Data

Find the `self.form_data` dictionary:

```python
self.form_data = {
    'email': 'reymarkcalex@gmail.com',
    'full_name': 'Reymark Calexterio',
    'contact_number': '09994956199',
    'complete_address': '53 Morato Avenue Damayan, Quezon City, Metro Manila, 1105'
}
```

Change the values to your own details.

#### ✏️ Save the File

Press **Ctrl+S**.

### 8. Place Your File in the Right Location

Make sure the file exists exactly at the path you set in step 7.

### 9. Start Chrome with Remote Debugging

**Close all Chrome windows** first.  
Open a **new Command Prompt** (not PowerShell) and run:

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug"
```

If Chrome is installed elsewhere, adjust the path.

- A new Chrome window will open. **Log into your Google account** (the same email you set in step 7).
- **Keep this Command Prompt window open** – the script will connect to this Chrome instance.

### 10. Run the Script

Go back to the PowerShell window (where your virtual environment is active) and run:

```powershell
python main.py
```

The script will now automate the process. Watch the terminal for progress.

### 11. Stop the Script

- Press **Ctrl+C** in the PowerShell window to stop early.
- The script will close the browser after finishing all submissions.

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'selenium'` | Activate the virtual environment: `.venv\Scripts\Activate.ps1` |
| Chrome doesn’t open with remote debugging | Ensure all Chrome windows are closed. Check the path to `chrome.exe`. |
| `WebDriverException: cannot find Chrome binary` | Chrome not installed in default location. Update the path in step 9. |
| File not found error | Verify the path in step 7A; the file must exist there. |
| Only the first “Add file” button works | The script closes the picker after each upload. If still failing, increase the `time.sleep()` delays. |
| Google sign‑in page appears | You didn’t log in during step 9. Log in in the Chrome window before running the script. |
| `pyautogui` types the path but doesn’t upload | The file dialog must be the active window. Don’t move the mouse or type during upload. |

---

## 🔧 Customization

### Change Number of Submissions

In `main.py`, near the end, find:

```python
bot.run_all(50)
```

Change `50` to any number.

### Change Text Fields

Edit the `self.form_data` dictionary as described in step 7.

### Change File to Upload

Modify the `self.file_path` line as described in step 7.

---

## 📁 Files in This Repository

| File | Description |
|------|-------------|
| `main.py` | The automation script |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation |

---

## 📜 License

This project is open‑source under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Credits

Built with 🐍 Python, [Selenium](https://selenium.dev), and [pyautogui](https://pyautogui.readthedocs.io/).  

---

**Happy automating!** 🚀