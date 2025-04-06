import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from hashing import hashfile



class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"🟢 Created: {event.src_path}")
        
    def on_modified(self, event):
        current_time = time.time()
        if not os.path.isdir(event.src_path):
            print(f"🟡 modified:{event.src_path}")

    def on_deleted(self, event):
        print(f"🔴 Deleted: {event.src_path}")


    def on_moved(self, event):
        print(f"🔵 Moved: from {event.src_path} to {event.dest_path}")

  

if __name__ == "__main__":
    root_directory = "/"
    path_to_watch = root_directory
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()
    print("moniterring started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
