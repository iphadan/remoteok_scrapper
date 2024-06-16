import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL="https://remoteok.com"
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
REQUEST_HEADER={
'User-Agent':USER_AGENT,
'Accept-Language':'en-US, en;q=0.5'
}

def getJobPosted():
    response=requests.get(url=BASE_URL,headers=REQUEST_HEADER,verify=False)
    return response.content.decode("utf-8-sig")

if __name__=="__main__":
    response=getJobPosted()
    
    print("=======>",response)

