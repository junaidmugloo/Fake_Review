from django.shortcuts import (get_object_or_404, render,redirect)
import logging
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
from su_admin.models import Category,Products,Order_items
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
    cart=Order_items.objects.filter(user_id=res.user.id).count(); 
    dict = {
        'dict': cat,
        'cart':cart
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
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name = request.POST.get('first_name')
        user=User.objects.filter(username=username)
        userEmail=User.objects.filter(email=email)
        if username!="" and email!="" and password!="":
            if user.count()>0:
                messages.info(request,"Username already taken")
                return JsonResponse({"error": "This username is already taken"}, status=400)
            elif userEmail.count()>0:
                return JsonResponse({"error": "This email is already taken"}, status=400)
            user=User.objects.create(email=email,username=username,first_name=first_name)
            user.set_password(password)
            user.save()
            return render(request,"signup2.html",{'success': 'Account created successfully'})
        else:
            return JsonResponse({"error": "error occurred"}, status=400)
    return render(request, 'signup2.html')


def product_detail(res,id):
    cart=Products.objects.filter(id=id);
    cart_data={
    'cart':cart
    }
    return render(res,"detail2.html",context=cart_data)

def product_shop(res):
    return render(res,"shop.html")

def product_cart(res):
    if res.method=='POST':
        qty_str=res.POST.get('product_qty')
        price_str=res.POST.get('product_price')
        try:
            qty = int(qty_str) if qty_str is not None else 0
        except ValueError:
            qty = 0

        try:
            price = float(price_str) if price_str is not None else 0.0
        except ValueError:
            price = 0.0
        
        total = price * qty
        product = get_object_or_404(Products, id=res.POST.get('product_id'))
        cart=Order_items.objects.create(product=product,
                                        user_id=res.POST.get('user_id'),
                                        qty=qty_str,
                                        price=price_str,
                                        total=total,
                                        status="cart",
                                        discount=""

                                        )
        cart.save()
    subtotal=0;
    cart=Order_items.objects.filter(user_id=res.user.id);  
    for i in cart:
        subtotal= subtotal + float(i.total)
    
    cart_data={
    'cart':cart,
    'sub':subtotal
    }

    return render(res,"cart.html",context=cart_data)


def delete_cart(res,id):
    item=Order_items.objects.filter(id=id);
    item.delete();
    return redirect('product_cart');


def product_contact(res):
    return render(res,"contact.html")

def product_checkout(res):
    if res.method=='POST':
        cart=Order_items.objects.filter(user_id=res.user.id);
        cart_data={
            'cart':cart,
             'tot':res.POST.get('Subtotal')
        }
        return render(res,"checkout.html",context=cart_data)
    return redirect('product_cart');


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

def front_logout(request):
    logout(request)
    return redirect('home')

#test case end