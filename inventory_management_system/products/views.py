from unicodedata import category
from webbrowser import get
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from products.models import product
from products.models import category


# Create your views here.

def viewproduct(request):
    pro= product.objects.all()
    context = {'pro':pro}
    return render(request,'products/viewproducts.html',context)

def listproduct(request):
    pro= product.objects.all()
    context = {'pro':pro}
    return render(request,'products/viewproducts.html',context)

def updateproduct(request):
    cate= category.objects.all()
    context = {'cate':cate}
    if request.method=='POST':
        prod = product()
        prod.product_name =request.POST.get('product_name')
        prod.category=category.objects.get(uid=request.POST['category'])
        prod.price = request.POST.get('price')
        prod.product_description=request.POST.get('description')
        if len(request.FILES) != 0:
            prod.image = request.FILES['product_image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect ('list_product')
        # prod_obj.product.product_name=product_name
    # return HttpResponse("this is product page")

    return render(request,'products/addproduct.html',context)

def addproduct(request):
    cate= category.objects.all()
    context = {'cate':cate}
    if request.method=='POST':
        prod = product()
        prod.product_name =request.POST.get('product_name')
        prod.category=category.objects.get(uid=request.POST['category'])
        prod.price = request.POST.get('price')
        prod.product_description=request.POST.get('description')
        if len(request.FILES) != 0:
            prod.image = request.FILES['product_image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect ('list_product')
        # prod_obj.product.product_name=product_name
    # return HttpResponse("this is product page")

    return render(request,'products/addproduct.html',context)


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
        return redirect('read_category')
    
    return render(request,'products/deletecategory.html',context)
