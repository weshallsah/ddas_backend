import sys
import hashlib
import base64


def hashfile(filename):


    BUF_SIZE = 65536

    sha256 = hashlib.sha256()


    with open( filename, 'rb') as f:
        while True:

            newdata=""
            data = f.read(BUF_SIZE)
            if  ".txt" in filename:
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



