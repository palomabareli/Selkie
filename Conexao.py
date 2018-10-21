#/usr/bin/python3
# -*- coding: UTF-8 -*-

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

def ConectDataBase():
    try:
        client = Cloudant( 
                "4637db36-4b7c-47d7-b006-6f846e72a22a-bluemix", 
                "ac21a13b101baabea9f1ea2594b622c54e7f2799b2f96fefb80173b37209ee12", 
                url="https://4637db36-4b7c-47d7-b006-6f846e72a22a-bluemix:ac21a13b101baabea9f1ea2594b622c54e7f2799b2f96fefb80173b37209ee12@4637db36-4b7c-47d7-b006-6f846e72a22a-bluemix.cloudant.com")

        client.connect()

        databaseName = "oguiadomochileirodasantarticas3"

        myDatabase = client.create_database(databaseName)

        if myDatabase.exists():
            print('{0} criado com sucesso'.format(databaseName))
        else:
            print('{0} não foi criado'.format(databaseName))

        client.disconnect()
    except Exception as ex:
        print(ex.message)

ConectDataBase()        