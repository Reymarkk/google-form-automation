Here's a polished, aesthetically pleasing README with clean formatting, emojis, and clear sections. It's still spoon‑feeding, but now looks professional on GitHub.

---

```markdown
# 🚀 Google Form Automation – Upload Files & Submit 50 Times

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/selenium-4.15+-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This Python script automates filling and submitting a Google Form **50 times** (or any number you choose). It:

- ✅ Fills text fields: **email, full name, contact number, complete address**
- 📎 Uploads the **same file** to **three separate “Add file” buttons** on the form
- 🔁 Automatically clicks “Submit another response” after each submission

Perfect for bulk submissions without repetitive manual work!

---

## 📋 Table of Contents

1. [How It Works](#-how-it-works)
2. [Prerequisites](#-prerequisites)
3. [Setup Instructions (Step‑by‑Step)](#-setup-instructions-step-by-step)
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
4. [Troubleshooting](#-troubleshooting)
5. [Customization](#-customization)
6. [Files in This Repository](#-files-in-this-repository)
7. [License](#-license)
8. [Credits](#-credits)

---

## ⚙️ How It Works

1. You start a Chrome browser **manually** with remote debugging enabled.  
2. You log into your Google account **once** in that browser.  
3. The Python script connects to that browser and:
   - Fills the form fields.
   - For each of the three “Add file” buttons:
     - Clicks the button.
     - Uploads your file using `pyautogui` (type the path + Enter).
     - Closes the file‑picker iframe.
   - Submits the form.
   - Clicks “Submit another response” (or refreshes if the link isn’t found).
4. The loop repeats until the desired number of submissions (default 50).

---

## 📌 Prerequisites

- **Windows** (the script uses absolute paths for Chrome and the file)
- **Python 3.7+** ([download](https://www.python.org/downloads/))
- **Google Chrome** (latest version)
- A file to upload (e.g., `calexterio_proof.jpg`) placed somewhere accessible
- A GitHub account (if you plan to clone the repo; not needed to run the script)

---

## 🛠️ Setup Instructions (Step‑by‑Step)

### 1. Install Python

- Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python for Windows.
- **During installation, check the box “Add Python to PATH”**.
- Open a new Command Prompt and verify with:
  ```cmd
  python --version
  ```
  You should see something like `Python 3.12.x`.

### 2. Create a Project Folder

Create a folder where you’ll keep the script, e.g.:

```
C:\Users\YourName\google-form-automation
```

### 3. Download the Script & Requirements

- Copy the `main.py` script from this repository into your folder.
- Create a file named `requirements.txt` and paste the following:

```txt
selenium>=4.15.0
webdriver-manager>=4.0.0
pyautogui>=0.9.54
```

### 4. Open PowerShell in the Folder

- In File Explorer, navigate to your project folder.
- Click **File** → **Open Windows PowerShell** (or **Shift** + right‑click and choose **Open PowerShell window here**).

### 5. Create & Activate a Virtual Environment

Run these commands one after the other:

```powershell
# Create the virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

If you get an execution policy error, run this once and then try again:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

You should now see `(.venv)` at the beginning of the PowerShell prompt.

### 6. Install Dependencies

```powershell
# Upgrade pip (recommended)
python -m pip install --upgrade pip

# Install everything from requirements.txt
pip install -r requirements.txt
```

### 7. **Customize the Script** (Crucial!)

Open `main.py` in a text editor (Notepad, VS Code, etc.). You **must** change a few lines to match your own information.

#### ✏️ File to Upload

Find this line near the top:

```python
self.file_path = "C:\\Users\\reyma\\Downloads\\calexterio_proof.jpg"
```

Replace it with the **full path** to your file.  
**Example:**  
If your file is `my_image.png` in `C:\Users\John\Downloads`:
```python
self.file_path = "C:\\Users\\John\\Downloads\\my_image.png"
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

Change the values to **your** own details (the ones you want to appear in the form).

#### ✏️ Save the File

Press **Ctrl+S** to save your changes.

### 8. Place Your File in the Right Location

Make sure the file exists exactly at the path you wrote in step 7. For example, if you set `self.file_path = "C:\\Users\\John\\Downloads\\my_image.png"`, that file must be there.

### 9. Start Chrome with Remote Debugging

**Close all Chrome windows** (this is important!).  
Then open a **new Command Prompt** (not PowerShell) and run:

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug"
```

If Chrome is installed somewhere else, adjust the path accordingly.

- A new Chrome window will open. **Log into your Google account** (the same email you set in step 7).
- You may also navigate to the form URL now, but the script will do it for you later.
- **Keep this Command Prompt window open** – the script will connect to this Chrome instance.

### 10. Run the Script

Go back to the PowerShell window (where your virtual environment is active) and run:

```powershell
python main.py
```

The script will:

- Connect to the already open Chrome window.
- Fill the text fields.
- For each of the three “Add file” buttons:
  1. Click the button.
  2. Wait for the file‑picker iframe.
  3. Upload the file (either directly via file input or using `pyautogui`).
  4. Close the iframe.
- Submit the form.
- Click “Submit another response” (or refresh if not found).
- Repeat for 50 submissions.

You’ll see progress messages in the terminal. If anything fails, a screenshot (`error_1.png`, `error_2.png`, …) will be saved in your project folder.

### 11. Stop the Script

- Press **Ctrl+C** in the PowerShell window to stop early.
- The script will automatically close the browser after finishing all submissions.

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'selenium'` | You forgot to activate the virtual environment. Run `.venv\Scripts\Activate.ps1` first. |
| Chrome doesn’t open with remote debugging | Close all Chrome windows. If the command still fails, check your Chrome installation path. |
| `WebDriverException: cannot find Chrome binary` | Chrome is not installed in the default location. Update the path in step 9. |
| File not found error | Double‑check the path in step 7A – the file must exist exactly there. |
| Only the first “Add file” button works | The script now properly closes the picker after each upload. If it still fails, try increasing the `time.sleep()` delays in `main.py`. |
| The script cannot find the “Add file” button | The form may load slowly. Increase the initial `time.sleep(5)` after loading the form. |
| Google sign‑in page appears | You didn’t log in during step 9. Log in in the Chrome window before running the script. |
| `pyautogui` types the path but doesn’t upload | Make sure the file dialog is the active window. Don’t move the mouse or type during upload. |

---

## 🔧 Customization

### Change the Number of Submissions

In `main.py`, near the end, find:

```python
bot.run_all(50)
```

Change `50` to any number (e.g., `100`).

### Change the Text Fields

Edit the `self.form_data` dictionary as described in step 7.

### Change the File to Upload

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

This project is open‑source under the **MIT License**. Feel free to use, modify, and share it.

---

## 🙌 Credits

Built with 🐍 Python, [Selenium](https://selenium.dev), and [pyautogui](https://pyautogui.readthedocs.io/).  

If you have any questions, open an issue on GitHub or contact the repository owner.

---

**Happy automating!** 🚀
```

---

This README uses proper markdown headings, code blocks, tables, emojis, and a table of contents. It's both visually appealing and highly readable on GitHub. The instructions are still spoon‑feeding, but now formatted cleanly.