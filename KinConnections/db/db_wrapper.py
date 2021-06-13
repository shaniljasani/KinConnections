import os

from airtable import Airtable


def db_add(user_object):
    userTable = Airtable('appHwa2pMKMmrkTKJ', os.environ['AIRTABLE_API_KEY'])
    userTable.create('Users', user_object)
    return