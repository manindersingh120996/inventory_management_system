from unicodedata import category
from webbrowser import get
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from products.models import product
from products.models import category


# Create your views here.
def addproduct(request):

    if request.method=='POST':
        product_name=request.POST.get('product name')
        category=request.POST.get('category')
        price=request.POST.get('price')
        product_description=request.POST.get('description')
        product_image=request.POST.get('oroduct img')
        prod_obj= product.objects.create(product_name=product_name, category=category, price=price, product_description=product_description,product_image=product_image)
        prod_obj.save()
        messages.success(request, 'Product Successfully ADDED')
        # prod_obj.product.product_name=product_name
    # return HttpResponse("this is product page")

    return render(request,'products/addproduct.html')

def readcategory(request):
    cate= category.objects.all()
    context = {'cate':cate}
    return render(request,'products/readcategory.html',context)

def updatecategory(request,uid):
    cate=category.objects.get(uid=uid)
    context = {'cate':cate}


    if request.method=='POST':
        name= request.POST.get('category_name')
        cat=category.objects.get(uid=uid)
        cat.category_name=name
        cat.save()
    
        messages.success(request, 'Category Updated Successfully')
        return redirect('view_category')

    # return HttpResponse("this is product page")
    return render(request,'products/updatecategory.html',context)

def deletecategory(request,uid):
    cate=category.objects.get(uid=uid)
    context = {'cate':cate}
    if request.method =="POST":
        cate.delete()
        messages.success(request, 'Category Deleted Successfully')
        return redirect('view_category')
    
    return render(request,'products/deletecategory.html',context)
