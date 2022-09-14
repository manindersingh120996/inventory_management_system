from django.contrib import admin
from accounts.views import login_page
from django.urls import path,include
from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', login_page, name="login")
]
