import os
import datetime
from hashing import hashfile
from sqlDB import create_database,insert_file,display_all_entries

exclude_dirs = [
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
    "temp",                # Temporary files
    "__pycache__",
]

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


async def scan_file_system(root_dir):
    print("started addeding")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")
        print(f"Directory names: {dirnames}")
        iscontinue = False
        for exdir in exclude_dirs:
            if(dirpath.find(exdir)!=-1):
                # print(exdir)
                iscontinue = True
                break
            

        if(iscontinue):
            continue
        

        for filename in filenames:
            iscontinue = False
            for exfile in exclude_files:
                if(filename == exfile):
                    iscontinue = True
                    break    

            if(iscontinue):
                continue
            
            for exdot in exclude_extensions:
                if(filename.find(exdot)!=-1):
                    iscontinue = True
                    break    

            if(iscontinue):
                continue

            hashcode = hashfile(dirpath + "\\" + filename)
            size = os.path.getsize(dirpath + "\\" + filename)
            ftime = os.path.getctime(dirpath + "\\" + filename)
            dtime = datetime.datetime.fromtimestamp(ftime)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(dirpath + "\\" + filename))
            print(hashcode)
            print(dtime)
            insert_file([filename,dirpath + "\\" + filename,size,dtime,mtime,hashcode])
    print("file added")
    return await display_all_entries()

            

            
    

# Example usage:
# root_directory = "."
# scan_file_system(root_directory)

