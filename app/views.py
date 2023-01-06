from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Cart
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView,DetailView
#def home(request):
 #return render(request, 'app/home.html')

class ProductView(ListView):
  model=Product
  fields=['id','title',' selling_price','discounted_price',
  'description',' product_image',]
  template_name = 'app/home.html'
  success_url='/product-detail/'

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 user=request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart/')

  
def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  amount= 0.0
  shipping_amount = 200
  totalamount = 0.0
  cart_prduct = [p for p in Cart.objects.all() if p.user == user]
  if cart_prduct:
   for p in cart_prduct:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount = amount + shipping_amount
  return render(request, 'app/addtocart.html',{'carts':cart, 
  'totalamount':totalamount, 'amount':amount})
 else:
   return render(request, 'app/emptycart.html')

def plus_cart(request):
  if request.method == 'GET':
    prod_id =request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount= 0.0
    shipping_amount = 200
    totalamount = 0.0
    cart_prduct = [p for p in Cart.objects.all() if p.user 
    == request. user]
    if cart_prduct:
     for p in cart_prduct:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
     
    data = {
    'quantity': c.quantity,
    'amount': amount,
    'totalamount':amount + shipping_amount
     }
    return JsonResponse(data)
  
def minus_cart(request):
  if request.method == 'GET':
    prod_id =request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount= 0.0
    shipping_amount = 200
    totalamount = 0.0
    cart_prduct = [p for p in Cart.objects.all() if p.user 
    == request. user]
    if cart_prduct:
     for p in cart_prduct:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      
    data = {
    'quantity': c.quantity,
    'amount': amount,
    'totalamount':amount + shipping_amount
     }
    return JsonResponse(data) 
def remove_cart(request):
  if request.method == 'GET':
    prod_id =request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    
    c.delete()
    amount= 0.0
    shipping_amount = 200
    totalamount = 0.0
    cart_prduct = [p for p in Cart.objects.all() if p.user 
    == request. user]
    if cart_prduct:
     for p in cart_prduct:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount

    data = {
    'amount': amount,
    'totalamount': amount + shipping_amount
     }
    return JsonResponse(data) 
  
