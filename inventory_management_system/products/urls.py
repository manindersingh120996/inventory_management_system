from django.contrib import admin
from accounts.views import login_page
from django.urls import path,include
from django.conf.urls.static import static
from products import views
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('product/', views.productaddpage, name="productsadd"),
    path('category/', views.categoryreadpage, name="AllCategory"),
    path('category/<str:id>/', views.categoryupdatepage, name="UpdateCategory"),
            
]