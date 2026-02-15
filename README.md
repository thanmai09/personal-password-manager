# Personal Password Manager 🔐

A simple yet secure local password manager built with Python and Streamlit. Store, view, search, and manage your passwords in a user-friendly web interface.

## Features

✨ **Add Passwords** - Store website credentials securely
👁️ **View All Passwords** - See all saved passwords with optional masking
🔍 **Search Passwords** - Find passwords by website name
🗑️ **Delete Passwords** - Remove old or no longer needed credentials
🛡️ **Password Masking** - Passwords are masked by default for security
🎨 **Clean UI** - Modern, responsive web interface

## Setup & Installation

### Prerequisites
- Python 3.7+
- pip

### Installation Steps

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
streamlit run app.py
```

3. **Access the app:**
   - The Streamlit app will automatically open in your browser
   - Default: http://localhost:8501

## How to Use

### Add a Password
1. Select "Add Password" from the menu
2. Enter website/service name, username/email, and password
3. Click "Save Password"

### View All Passwords
1. Select "View Passwords" from the menu
2. Passwords are displayed in a masked table
3. Enable "Show passwords" checkbox to reveal them (use with caution!)

### Search Password
1. Select "Search Password" from the menu
2. Enter the website name you want to search
3. View matching results

### Delete Password
1. Select "Delete Password" from the menu
2. Select the website to delete
3. Click "Delete Selected Password"

## Security Notes ⚠️

- Passwords are stored in plain text in `passwords.txt`
- **Keep this file secure and never share your device**
- For production use, consider encrypted storage solutions
- Don't use this for sensitive accounts without encryption
- Always keep backups of your passwords

## File Structure

```
personal-password-manager/
├── app.py                 # Streamlit web application
├── password_manager.py    # Original CLI version
├── passwords.txt          # Stored passwords (created on first use)
├── requirements.txt       # Python dependencies
├── streamlit_config.toml  # Streamlit configuration
└── README.md             # This file
```

## Original CLI Version

The original command-line version is still available in `password_manager.py`. Run it with:
```bash
python password_manager.py
```

## License

Personal use only. Handle with care!
