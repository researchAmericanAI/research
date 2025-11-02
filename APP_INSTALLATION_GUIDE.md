# re:search Mac App Installation Guide

## Quick Start

1. **Download** the `re:search.app` bundle
2. **Move** `re:search.app` to your Applications folder (or anywhere you like)
3. **Double-click** `re:search.app` to launch

That's it! No Terminal commands needed.

## First Launch

On first launch, you may see a security warning saying "re:search.app cannot be opened because it is from an unidentified developer."

To fix this:
1. Go to **System Preferences** → **Security & Privacy** → **General**
2. Click **"Open Anyway"** next to the message about re:search.app
3. Click **"Open"** in the confirmation dialog

Alternatively, you can **right-click** (or Control-click) on `re:search.app` and select **"Open"** from the menu.

## Prerequisites

Before using re:search, make sure you have:

1. **Python 3.6+** installed (download from https://python.org if needed)
2. **Ollama** installed and running (download from https://ollama.ai)

## First-Time Setup

The first time you launch re:search:
- A virtual environment will be created automatically
- Dependencies will be installed
- This may take 30-60 seconds

Subsequent launches will be much faster!

## Usage

Once launched:
- The backend server starts automatically
- Your browser will open to the re:search interface
- Keep the app running - don't close the Terminal window that appears

To stop re:search:
- Press **Ctrl+C** in the Terminal window, or
- Quit the Terminal application

## Troubleshooting

### "Ollama is not running" error
Start Ollama before launching re:search.

### "Python 3 is required" error
Install Python 3.6 or higher from https://python.org

### App won't open at all
Make sure you've allowed the app in Security & Privacy settings (see "First Launch" above).

## Support

For issues or questions:
- Check the README.md inside the app bundle (right-click → Show Package Contents → Contents → Resources)
- Visit: https://ko-fi.com/researchkofi

---

**Note:** The app bundle contains all necessary files. You can move or rename it freely - everything will continue to work!
