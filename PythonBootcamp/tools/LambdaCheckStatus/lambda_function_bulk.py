#!/usr/bin/env python
import urllib
import urllib.request
#import urllib2
import datetime
import time
import boto3
import os
from bs4 import BeautifulSoup
import csv

#number = os.environ['dataNumber']
statuses = {}
totalApproved = 0
processedButNotApproved = 0
total = 0
filename = '/caseFile.csv'


def checkStatus(number):
    statusMsg= ""
    global totalApproved
    global total
    global caseWriter
    global cases
    global processedButNotApproved

    time = datetime.datetime.now()
    timeStr = time.strftime('%Y-%b-%d %H:%M:%S')
    try:
        status = getStatus(number)
        if 'Not a I-129' in str(status):
            pass
        else:
            total += 1
            if [number] not in cases:
                caseWriter.writerow([number])

        #print(timeStr + ' -- receipt number: [' + number + '], case status: [' + status + ']')
        if "Approved".upper() in str(status).upper():
            statusMsg = "YAY!!! Approved"
            statuses[number] = 1
            print(str(number) + ',' + str(1))
            totalApproved += 1

        elif 'Not a I-129' in str(status):
            pass
            #print(str(number) + ',' + str(0))
            #print(str(number) + ',' + str(0))

        elif  "Received".upper() in str(status).upper() and "emailed".upper() in str(status).upper():
            statuses[number] = 0
            print(str(number) + ',' + str('not processed yet!'))
        elif "Received".upper() in str(status).upper():
            statuses[number] = 0
            print(str(number) + ',' + str('not processed yet! Not Premium'))

        elif not "Received".upper() in str(status).upper():
            statusMsg = "Ohh no!!! " + status
            statuses[number] = 0
            print(str(number) + ',' + str(-1))
            processedButNotApproved +=1

    except AttributeError:
        statusMsg = 'Invalid receipt number: [' + number + '], please check your receipt number and try again'

    #for key,value in statuses:
     #   print(key)
     #   print (value)




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
    #print(soup)

    #check i-129:

    rowTag = soup.find('div', {'class': 'rows text-center'})
    rowContents = rowTag.text.split("\n")
    #print(rowContents)

    # print(rowContents)


    content ="Not a I-129"


    for word in rowContents:
        if "I-129" in str(word):
            statusTag = soup.find('div', {'class': 'current-status-sec'})
            contents = statusTag.text.split("\n")
            content = contents[2].strip()
            break
        #print(statusTag)

    return content

cases =[]
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cases.append(row)

casefile =  open(filename, mode='a')
caseWriter= csv.writer(casefile, quotechar='"', quoting=csv.QUOTE_MINIMAL)



useFile = 1



if useFile == 1:
    for number in cases:

        checkStatus(str(number[0]))

else:
    for i in range(900,1000):
        numCounter =  1923650000 + i
        number =  "WAC" + str(numCounter)
        checkStatus(number)

casefile.close()

if total != 0 :
    pending = total - (totalApproved + processedButNotApproved)
    print(f'\n\nTotal Approved: {totalApproved} of {total}  with approved percentage of {(totalApproved/total) *100}%  \n'
          f'\nProcessed But not yet approved: {processedButNotApproved} , percentage: {(processedButNotApproved/total) *100}% \n'
          f'\nPending: {pending}, percentage: {(pending/total) *100}%')
