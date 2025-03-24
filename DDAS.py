# import hashlib

# content = "Random String"
# hash_object = hashlib.sha256(content.encode('utf-8'))  
# hex_dig = hash_object.hexdigest()

# print(f"Hashed String: {hex_dig}")


# # Original hashed content storage
# # original_digest = "45a5c98b092b9b67b3581fbe482749cd90d0a307a8d3c30701641b3a1921d944"  

# # Content to verify 
# verify_data = "My important data to verify!"

# # Generate hash
# verify_hash = hashlib.sha256(verify_data.encode('utf-8')).hexdigest() 

# # Compare hashes
# if verify_hash == hex_dig:
#     print("file match") 
# else:
#     print("file does not match")

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

            print(data)
            
            if not data:
                break

            if newdata:
                print(newdata.encode("utf-8"))
                sha256.update(newdata.encode("utf-8"))

            else :
                sha256.update(data)

    return sha256.hexdigest()



file_hash = hashfile("file.txt")

file_hash1 = hashfile("test.txt")

if(file_hash==file_hash1):
    print("file is same")

else:
    print("file is not same")

print(f"Hash : {file_hash}")
print(f"Hash : {file_hash1}")