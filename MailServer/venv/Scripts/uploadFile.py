import ftplib
import os

def upload(ftp, file):
    print('Inside upload fn....')
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)


print('Before ftp variable is loaded...')
ftp = ftplib.FTP("ftp.nluug.nl")
print("About to login....")
ftp.login("anonymous", "ftplib-example-1")
print("Login Successful....")
#ftp.cwd('/pub/')         # change directory to /pub/
upload(ftp, "shiva.txt")
print('Upload successful....')