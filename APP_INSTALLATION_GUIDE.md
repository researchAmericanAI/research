# re:search Mac App Installation Guide

## Installation

1. **Download** `re:search.app`
2. **Drag** `re:search.app` to your **Applications** folder
3. **Double-click** `re:search.app` to launch
4. You'll see a security warning that the app can't be opened
5. Go to **System Settings** → **Privacy & Security**
6. Scroll down and click **"Open Anyway"** next to the re:search message
7. Click **"Open"** in the confirmation dialog

**That's it!** After the first launch, you can simply double-click the app normally.

> **Note:** This security step is only needed the first time for unsigned apps.

## Automatic Python Installation

**Don't have Python?** No problem!

If Python 3 is not installed, re:search will:
1. Detect that Python is missing
2. Offer to install it automatically using Homebrew
3. Guide you through the installation (takes 5-10 minutes)

Click **"Yes"** when prompted to proceed with automatic installation.

## Prerequisites

**Required:**
- **Ollama** - Download from [ollama.ai](https://ollama.ai)

**Optional (auto-installed if missing):**
- **Python 3.6+** - Will be installed automatically via Homebrew if not present

## First-Time Setup

The first time you launch re:search:
- A virtual environment will be created in your home folder (`~/.research_venv`)
  - This avoids macOS App Translocation security issues
  - The app bundle itself remains clean and portable
- Dependencies will be installed
- This may take 30-60 seconds

Subsequent launches will be much faster!

## Usage

When you launch re:search:
- The backend server starts automatically
- Your browser opens to the interface
- A Terminal window appears (keep it open while using the app)

To quit:
- Press **⌘Q** or close the Terminal window
- Or press **Ctrl+C** in the Terminal

## Troubleshooting

### Security warning / Can't open the app
1. Try to open the app (it will be blocked)
2. Go to **System Settings** → **Privacy & Security**
3. Scroll down and click **"Open Anyway"**
4. Try opening the app again and click **"Open"** in the dialog

### "Ollama is not running"
Start the Ollama app before launching re:search.

### "Python 3 is required"
Click "Yes" when prompted to install automatically. If this fails, download Python from [python.org](https://python.org).

### Need to uninstall?
Simply delete `re:search.app` from Applications and `~/.research_venv` from your home folder.

## Support

Questions or issues? Visit [ko-fi.com/researchkofi](https://ko-fi.com/researchkofi)

---

**Tech Details:** Virtual environment stored at `~/.research_venv` • App is portable and can be moved freely
