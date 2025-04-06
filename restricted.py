
exclude_dirs = {
    "windows",            # System files and logs
    "system32",           # Core system files
    "syswow64",           # 32-bit system files on 64-bit systems
    "program files",      # Installed applications
    "program files (x86)",# 32-bit applications
    "programdata",        # Shared app data
    "appdata",            # User-specific app data
    "local",              # Local app data (inside AppData)
    "roaming",            # Roaming app data (inside AppData)
    "locallow",           # Low-integrity app data (inside AppData)
    "temp"                # Temporary files
}

exclude_extensions = {
    ".log",      # Log files with potential user activity
    ".dat",      # Data files (e.g., NTUSER.DAT)
    ".ini",      # Configuration files
    ".db",       # Database files
    ".sqlite",   # SQLite database files
    ".bak"       # Backup files
}

exclude_files = {
    "passwords.txt",    # Common password storage
    "credentials.json", # Credential files
    "config.ini",       # Generic config file
    "ntuser.dat"        # User registry hive
}

