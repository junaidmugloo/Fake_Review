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
from su_frontend import views as front
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('su/',su.index),

    #admin login from admin panel or django admin
    path('su/login',su.login),
    path('su/logout',su.logout_view),
   
    #product routing
    path('su/add/products',su.add_product),
    path('su/view/products',su.view_product),
     path('su/products/delete/<id>',su.delete_product),
    # category routing
    path('su/category',su.category),
    path('su/category/delete/<id>',su.category_delete),


    #front end routing
     path('', front.front_index, name='front_index'),
     path('login/', front.front_login, name='front_login'),
     path('signup/', front.front_signup, name='front_signup'),
     path('product/detail/', front.product_detail, name='product_detail'),
     path('shop/', front.product_shop, name='product_shop'),
     path('contact/', front.product_contact, name='product_contact'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
