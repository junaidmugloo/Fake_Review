from django.shortcuts import (render,redirect)
import logging
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
from su_admin.models import Category,Products
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,logout,login)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from textblob import TextBlob

client = MongoClient('mongodb://localhost:27017/')
category_db = client['fake_review']
logger = logging.getLogger(__name__)

# Create your views here.

def front_index(res):
    cat=Products.objects.all() 
    dict = {
        'dict': cat
        }
    return render(res,'index2.html',context=dict);

def front_login(res):
    if res.method == 'POST':
        form = AuthenticationForm(res, data=res.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and not user.is_superuser:
                login(res, user)
                return redirect('home')
            else:
                return render(res,"login2.html",{'error': 'Admin account can''t login '})
        else:
            return render(res,"login2.html",{'error': 'Wrong username or password'})
    else:
        form = AuthenticationForm()
        return render(res,"login2.html",{'form': form})

def front_signup(request):
   
   
    if request.method == 'POST':
        email=request.POST.get('email');
        username=request.POST.get('username');
        password=request.POST.get('password');
        user=User.objects.filter(username=username)
        if user.count()>0:
            messages.info(request,"Username already taken")
            return render(request,"signup2.html",{'error': 'Username already taken'})
        user=User.objects.create(email=email,username=username)
        user.set_password(password)
        user.save()
        return render(request,"signup2.html",{'error': 'Account created successfully'})
       
    return render(request, 'signup2.html')


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
        email=request.POST.get('email');
        username=request.POST.get('username');
        password=request.POST.get('password');
        user=User.objects.create(email=email,username=username)
        user.set_password(password)
        user.save()
    else:
       return render(request, 'signup2.html')



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