import ftplib
import sys

def getFile(ftp, filename):
    try:
        print("calling retrbinary fn to fecth file")
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print ("Error")


ftp = ftplib.FTP("ftp.nluug.nl")
print("About to login....")
ftp.login("anonymous", "ftplib-example-1")
print("Login Successful....")
ftp.cwd('/pub/')         # change directory to /pub/
#getFile(ftp,'README.nluug')
getFile(ftp,'robots.txt')
print('File downloaded....')
ftp.quit()
