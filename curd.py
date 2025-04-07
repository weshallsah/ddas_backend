import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from hashing import hashfile
from sqlDB import create_database,insert_file,display_all_entries

recently_modified = {}

observer = Observer()



class MyHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"🟢 Created: {event.src_path}")

    def on_modified(self, event):
        global recently_modified
        current_time = time.time()

        if event.src_path in recently_modified and current_time - recently_modified[event.src_path] < 2:
            return
        recently_modified[event.src_path] = current_time
        if(os.path.isfile(event.src_path)):
            if(event.src_path.find(".tmp") != -1):
                return
            print(f"🟡 Modified: {event.src_path}")
            filename = os.path.basename(event.src_path)
            hashcode = hashfile(filename,event.src_path)
            size = os.path.getsize(event.src_path)
            ftime = os.path.getctime(event.src_path)
            dtime = datetime.datetime.fromtimestamp(ftime)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(event.src_path))
            insert_file([filename,event.src_path,size,dtime,mtime,hashcode])
            

    def on_deleted(self, event):
        print(f"🔴 Deleted: {event.src_path}")


    def on_moved(self, event):
        print(f"🔵 Moved: from {event.src_path} to {event.dest_path}")


  

def StartMonitor():
    root_directory = "/"
    path_to_watch = root_directory
    event_handler = MyHandler()
    
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()
    print("moniterring started")
    return "moniter started"
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    

def stopMonitor():
    observer.stop()
    return "monitering stoped"
