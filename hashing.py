import sys
import hashlib
import base64


def hashfile(filename,path):


    BUF_SIZE = 65536

    sha256 = hashlib.sha256()

    ext = filename.split('.')
    print(ext[-1])
    sha256.update(ext[-1].encode("utf-8"))

    with open( path, 'rb') as f:
        while True:

            newdata=""
            data = f.read(BUF_SIZE)
            if  ".txt" in path:
                newdata = data.decode("utf-8").strip().replace('\r\n','').replace(' ','')

            # print(data)
            
            if not data:
                break

            if newdata:
                print(newdata.encode("utf-8"))
                sha256.update(newdata.encode("utf-8"))

            else :
                sha256.update(data)

    return sha256.hexdigest()

# hash1 = hashfile("hhtth.txt","./folder/hhtth.txt")
# hash2 = hashfile("style.css","./folder/style.css")
# print(hash1)
# print(hash2)
# if(hash2==hash1):
#     print("file is same")
# else:
#     print("file is not same")
