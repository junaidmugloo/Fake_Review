from django.shortcuts import render

# Create your views here.

def front_index(res):
    return render(res,"index2.html")