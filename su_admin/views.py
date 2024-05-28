from django.shortcuts import render
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['fake_review']
# Create your views here.
def index(res):
    return render(res,'index.html');

def login(res):
    return render(res,'login.html');
