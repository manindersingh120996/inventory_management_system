from django.contrib import admin
from accounts.views import login_page
from django.urls import path,include
from django.conf.urls.static import static
from accounts import views
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.login_page, name="login"),
    path('login1', views.loginpage, name="login1"),
    path('register', views.registerpage, name="register"),
    
]

