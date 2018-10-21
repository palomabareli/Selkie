#/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests

cl_username = "4637db36-4b7c-47d7-b006-6f846e72a22a-bluemix"
cl_password = "ac21a13b101baabea9f1ea2594b622c54e7f2799b2f96fefb80173b37209ee12"
cl_database = "oguiadomochileirodasantarticas3"

folder = '/home/paloma/Documents/Estudos/DataBase/BaseDerivad/'
fileJSON = 'serienova.json'

folderFileJSON = folder + fileJSON

try:
    json = open(folderFileJSON, 'r')

    response = requests.post(
        "https://" + cl_username + ".cloudant.com/" + cl_database,
        data=json,
        auth=(cl_username, cl_password),
        headers = {'Content-type': 'application/json'}
    )

    #print(response)

    if (response.status_code == 200):
        print("OK: " + response.json() + "Status Code:" + str(response.status_code))
    else:
        print("ERROR: " + response.text + "Status Code:" + str(response.status_code))
except Exception as ex:
    print(ex.message)  

