#! /usr/bin/env python3
import os
import requests
import json

def readcomment(directory,f):
    coms =[]
    txtfile = open(directory+f ,"r")
    txtfile = txtfile.readlines()
    for lines in txtfile:
        lines = lines.rstrip()
        #print(lines) # type:str
        coms.append(lines)
    #print(coms)
    return coms

def listodict(com):
    heading = ['title', 'name', 'date','feedback']
    commentdict = {}
    commentdict = {heading : com for heading, com in zip(heading, com)}
    #print(commentdict)
    return commentdict

def readuploadfile(directory):
    file = os.listdir(directory)
    #print(file)
    for f in file :

        comment = readcomment(directory,f)
        comdict = listodict(comment)
        response = requests.post("http://34.72.125.126/feedback/", data=comdict )
        print(response.status_code)

    return comdict

comments = readuploadfile('/data/feedback/')
