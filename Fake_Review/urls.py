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
     path('', front.front_index, name='home'),
     path('login/', front.front_login, name='front_login'),
     path('signup/', front.front_signup, name='front_signup'),
     path('product/detail/', front.product_detail, name='product_detail'),
     path('shop/', front.product_shop, name='product_shop'),
     path('contact/', front.product_contact, name='product_contact'),
     path('cart/', front.product_cart, name='product_cart'),
     path('checkout/', front.product_checkout, name='product_checkout'),

#analyze
 path('analyze/', front.analyze_sentiment, name='analyze_sentiment'),

#test case start
 path('test/', front.signup_view, name='signup_view'),
 path('test2/', front.login_view, name='login_view'),
#test case end

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
