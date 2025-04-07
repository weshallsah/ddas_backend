
from sqlDB import create_database,insert_file,display_all_entries,search_file,deletefile
from scansys import scan_file_system
from curd import stopMonitor,StartMonitor

from typing import Union

from fastapi import Body, FastAPI

app = FastAPI()


conn, cursor = create_database()

@app.get("/scan")
async def scan():
    root_directory = "D:\project\demo"
    return await scan_file_system(root_directory)

@app.get("/getdata")
async def getData():
    result = await display_all_entries()
    return result

@app.get("/startmoniter")
def StartMoniter():
    return StartMonitor()

@app.get("/stopmoniter")
def StopMoniter():
    return stopMonitor()

# @app.post("/search")
def Search():
    search_file()

@app.delete("/delete/{id}")
async def delete(id):
    print(f"id:= {id}")
    # return f"{id} and {path}"
    await deletefile(id)
    return await scan()
    return f"id:= {id}"
