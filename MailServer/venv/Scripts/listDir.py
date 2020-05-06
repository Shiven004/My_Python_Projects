import ftplib
import os
import stat



def listDir():
    #ftp = ftplib.FTP("ftp.nluug.nl")
    #ftp.login("anonymous", "ftplib-example-1")
    ftp = ftplib.FTP("192.168.1.11")
    ftp1.login("sk0409", "$omsairam4S0409")
    print("Hello world...")
    data = []
    #ftp.cwd('/pub/')  # change directory to /pub/
    #os.chmod('/pub', 0o777)  # for example
    ftp1.dir(data.append)
    ftp1.quit()
    for line in data:
        print ("--------->", line)


listDir()