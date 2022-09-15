from django.contrib import admin
from accounts.views import login_page
from django.urls import path,include
from django.conf.urls.static import static
from products import views
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('product/', views.addproduct, name="add_product"),
    path('category/', views.readcategory, name="view_category"),
    path('category/<str:uid>/', views.updatecategory, name="update_category"),
    path('category/<str:uid>/', views.deletecategory, name="delete_category"),

]