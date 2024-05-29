from django.shortcuts import (render,HttpResponseRedirect,redirect)
import json
from django.http import HttpResponse
from pymongo import MongoClient
from su_admin.models import Category,Products
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,logout,login)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as cslogin
from textblob import TextBlob
from .forms import SignUpForm
client = MongoClient('mongodb://localhost:27017/')
category_db = client['fake_review']

# Create your views here.

def front_index(res):
    cat=Products.objects.all() 
    dict = {
        'dict': cat
        }
    return render(res,'index2.html',context=dict);

def front_login(res):
    return render(res,"login2.html")

def front_signup(res):
    return render(res,"signup2.html")

def product_detail(res):
    return render(res,"detail2.html")

def product_shop(res):
    return render(res,"shop.html")

def product_cart(res):
    return render(res,"cart.html")

def product_contact(res):
    return render(res,"contact.html")

def product_checkout(res):
    return render(res,"checkout.html")


#analyzer
def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity

            return render(request, 'analyzer/result.html', {'text': text, 'sentiment_score': sentiment_score})

    return render(request, 'analyzer/setup.html')



#test case

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'check.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'check2.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

#test case end