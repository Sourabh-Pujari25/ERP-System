from dotenv import load_dotenv
import os
import streamlit as st
from pymongo import MongoClient
from pprint import pprint 

#--IMPORT PATHS----------

load_dotenv()
IMAGES=os.getenv("IMAGES")
LOGO_IMAGE=os.getenv("LOGO_IMAGE")

CONNECTION_URL=os.getenv("CONNECTION_URL")
DATABASE_NAME=os.getenv("DATABASE_NAME")

client=MongoClient(CONNECTION_URL)

vardhaman_data=client[DATABASE_NAME]
users=vardhaman_data["users"]

def add_user():
    user={"Username":"Sourabh","Password":"Pujari"}
    response = users.insert_one(user)

    return response.acknowledged



def get_user():
    response=users.find()

    for i in response:
        print(i)
    return response



def update_user():
    response=users.update_one({"Username":"Sourabh"},{"$set":{"Username":"Pujari"}})

    return response.acknowledged



print(get_user())
# add_user()
# print(update_user())