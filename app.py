import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Password Manager",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
    }
    .success {
        color: #27ae60;
        font-weight: bold;
    }
    .warning {
        color: #e74c3c;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='header'>🔐 Personal Password Manager</h1>", unsafe_allow_html=True)

# Initialize file path
PASSWORD_FILE = "passwords.txt"

def ensure_file_exists():
    """Create passwords.txt if it doesn't exist"""
    if not os.path.exists(PASSWORD_FILE):
        open(PASSWORD_FILE, 'a').close()

def add_password(site, username, password):
    """Add a password to the file"""
    ensure_file_exists()
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{site} | {username} | {password}\n")
    return True

def view_passwords():
    """Read and return all passwords"""
    ensure_file_exists()
    with open(PASSWORD_FILE, "r") as file:
        content = file.read()
    return content

def search_password(search_site):
    """Search for a password by site"""
    ensure_file_exists()
    results = []
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            if search_site.lower() in line.lower():
                results.append(line.strip())
    return results

def delete_password(site_name):
    """Delete a password entry"""
    ensure_file_exists()
    lines = []
    with open(PASSWORD_FILE, "r") as file:
        lines = file.readlines()
    
    with open(PASSWORD_FILE, "w") as file:
        for line in lines:
            if site_name.lower() not in line.lower():
                file.write(line)
    return True

# Sidebar navigation
st.sidebar.header("Menu")
option = st.sidebar.radio(
    "Choose an action:",
    ["Add Password", "View Passwords", "Search Password", "Delete Password"]
)

# Main content area
if option == "Add Password":
    st.subheader("➕ Add New Password")
    
    col1, col2 = st.columns(2)
    with col1:
        site = st.text_input("Website/Service Name", key="site_input")
        username = st.text_input("Username/Email", key="user_input")
    
    with col2:
        password = st.text_input("Password", type="password", key="pass_input")
    
    if st.button("Save Password", use_container_width=True):
        if site and username and password:
            try:
                add_password(site, username, password)
                st.success("✅ Password saved successfully!", icon="✅")
                st.balloons()
            except Exception as e:
                st.error(f"Error saving password: {e}")
        else:
            st.warning("⚠️ Please fill in all fields!")

elif option == "View Passwords":
    st.subheader("👁️ View All Passwords")
    
    try:
        content = view_passwords()
        if content.strip():
            st.info("📋 All saved passwords:")
            
            # Display as a formatted table
            lines = content.strip().split('\n')
            if lines and lines[0]:
                st.table({
                    "Website": [line.split(" | ")[0] for line in lines],
                    "Username": [line.split(" | ")[1] for line in lines],
                    "Password": ["•" * len(line.split(" | ")[2]) for line in lines]  # Masked display
                })
                
                # Show option to reveal passwords
                if st.checkbox("Show passwords (⚠️ Security Risk)"):
                    st.warning("Make sure no one is looking at your screen!")
                    for line in lines:
                        if line.strip():
                            parts = line.split(" | ")
                            st.text(f"{parts[0]} | {parts[1]} | {parts[2]}")
            else:
                st.info("No passwords saved yet!")
        else:
            st.info("No passwords saved yet!")
    except Exception as e:
        st.error(f"Error reading passwords: {e}")

elif option == "Search Password":
    st.subheader("🔍 Search Password")
    
    search_term = st.text_input("Enter website name to search:")
    
    if st.button("Search", use_container_width=True):
        if search_term:
            try:
                results = search_password(search_term)
                if results:
                    st.success(f"Found {len(results)} match(es)!")
                    for result in results:
                        parts = result.split(" | ")
                        if len(parts) == 3:
                            col1, col2, col3 = st.columns(3)
                            col1.write(f"**Website:** {parts[0]}")
                            col2.write(f"**Username:** {parts[1]}")
                            col3.write(f"**Password:** {'•' * len(parts[2])}")
                else:
                    st.info(f"No passwords found for '{search_term}'")
            except Exception as e:
                st.error(f"Error searching: {e}")
        else:
            st.warning("Please enter a website name to search!")

elif option == "Delete Password":
    st.subheader("🗑️ Delete Password")
    
    try:
        content = view_passwords()
        if content.strip():
            lines = content.strip().split('\n')
            sites = [line.split(" | ")[0] for line in lines if " | " in line]
            
            if sites:
                site_to_delete = st.selectbox("Select website to delete:", sites)
                
                if st.button("Delete Selected Password", use_container_width=True):
                    delete_password(site_to_delete)
                    st.success(f"✅ Password for '{site_to_delete}' deleted successfully!")
                    st.rerun()
            else:
                st.info("No passwords to delete!")
        else:
            st.info("No passwords saved yet!")
    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>⚠️ Store this securely and don't share your device!</p>", unsafe_allow_html=True)
