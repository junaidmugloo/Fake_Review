from django.shortcuts import (render,HttpResponseRedirect)
from pymongo import MongoClient
from .models import Category
client = MongoClient('mongodb://localhost:27017/')
category_db = client['su_admin_products']
# Create your views here.

#dashboard
def index(res):
    return render(res,'index.html');
#admin login
def login(res):
    return render(res,'login.html');
# add product
def add_product(res):
    return render(res,'add_product.html');
# view product
def view_product(res):
    return render(res,'view_product.html');
# add category and view category
def category(res):
    if res.method=="POST":
        category_db= Category(name=res.POST['category'])
        category_db.save()
        return render(res,'category.html');
    else:
        cat=Category.objects.all()
       
        dict = {
        'dict': cat
        }
        return render(res,'category.html',context=dict);
#delete category
def category_delete(res,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect("/su/category")

