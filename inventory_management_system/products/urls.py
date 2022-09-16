from django.contrib import admin
from accounts.views import login_page
from django.urls import path,include
from django.conf.urls.static import static
from products import views
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add/', views.addproduct, name="add_product"),
    path('view/', views.viewproduct, name="view_product"),
    path('list/', views.listproduct, name="list_product"),
    path('update/<str:uid>', views.updateproduct, name="update_product"),
    path('delete/<str:uid>', views.deleteproduct, name="delete_product"),
    

    path('read/', views.readcategory, name="read_category"),
    path('update/<str:uid>/', views.updatecategory, name="update_category"),
    path('delete/<str:uid>/', views.deletecategory, name="delete_category"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)