#!/usr/bin/env python
import urllib
import urllib.request
#import urllib2
import datetime
import time
import boto3
import os
from bs4 import BeautifulSoup


number = os.environ['dataNumber']



def sendSNS(message):

    # Create an SNS client
    sns = boto3.client('sns')

    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        TopicArn='',
        Subject = message,
        Message = message
    )

def checkStatus(event, context):
    statusMsg= ""
    time = datetime.datetime.now()
    timeStr = time.strftime('%Y-%b-%d %H:%M:%S')
    try:
        status = getStatus(number)
        print(timeStr + ' -- receipt number: [' + number + '], case status: [' + status + ']')
        if status == "Case Was Received and A Receipt Notice Was Emailed":
            statusMsg ="Wait its not yet processed!!!"
        else:
            if "Approved" in status:
                statusMsg = "YAY!!! Approved"
            else:
                statusMsg = "Ohh no!!! " + status

    except AttributeError:
        statusMsg = 'Invalid receipt number: [' + number + '], please check your receipt number and try again'

    if (statusMsg != "Wait its not yet processed!!!"):
        sendSNS(statusMsg)



def getStatus(receiptNumber):
    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
    # changeLocale=&appReceiptNum=YSC1790007419&initCaseSearch=CHECK+STATUS
    values = {'changeLocale': '',
              'appReceiptNum': receiptNumber,
              'initCaseSearch': 'CHECK STATUS'}
    data = urllib.parse.urlencode(values).encode("utf-8")

    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read()

    soup = BeautifulSoup(the_page, 'html.parser')
    statusTag = soup.find('div', {'class': 'current-status-sec'})

    contents = statusTag.text.split("\n")
    content = contents[2].strip()

    return content

