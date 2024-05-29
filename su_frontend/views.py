from django.shortcuts import render

# Create your views here.

def front_index(res):
    return render(res,"index2.html")

def front_login(res):
    return render(res,"login2.html")

def front_signup(res):
    return render(res,"signup2.html")

def product_detail(res):
    return render(res,"detail2.html")

def product_shop(res):
    return render(res,"shop.html")

def product_contact(res):
    return render(res,"contact.html")
