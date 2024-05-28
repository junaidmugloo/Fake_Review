"""
URL configuration for Fake_Review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from su_admin import views as su
from su_frontend import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('su/',su.index),
    path('su/login',su.login),
    #product routing
    path('su/add/products',su.add_product),
    path('su/view/products',su.view_product),
    # category routing
    path('su/category',su.category),
    path('su/category/delete/<id>',su.category_delete),
   

]
