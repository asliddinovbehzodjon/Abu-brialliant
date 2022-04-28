from django.shortcuts import redirect, render
from .models import Customer, OrderItem, Products,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from django.contrib.auth.decorators import login_required
def store(request):
     if request.user.is_authenticated:
        user=request.user
        customer = Customer.objects.get(user = user)
        order,created=Order.objects.get_or_create(customer=customer)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
     else:
        items=[]
        order={'get_cart_items':0}
        cartItems=order['get_cart_items']
     products=Paginator(Products.objects.all(),per_page=6)
     page=request.GET.get('page')
     try:
          products=products.page(page)
     except PageNotAnInteger:
          products=products.page(1)
     except EmptyPage:
          products=products.page(products.num_pages)
     context = {'products':products,'cartItems':cartItems}
     return render(request,'store.html',context=context)
def product_detail(request,id):
     if request.user.is_authenticated:
        user=request.user
        customer = Customer.objects.get(user = user)
        order,created=Order.objects.get_or_create(customer=customer)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
     else:
        items=[]
        order={'get_cart_items':0}
        cartItems=order['get_cart_items']
     product = Products.objects.get(id = id)
     context = {'product':product,'cartItems':cartItems}
     return render(request,'detail.html',context=context)
def card(request):
     if request.user.is_authenticated:
        user=request.user
        customer = Customer.objects.get(user = user)
        order,created=Order.objects.get_or_create(customer=customer)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
     else:
        items=[]
        order={'get_cart_items':0}
        cartItems=order['get_cart_items']
     context={'items':items,'order':order,'cartItems':cartItems}
     return render(request,'card.html',context = context)
@login_required(login_url='login')
def checkout(request):
     if request.user.is_authenticated:
          user=request.user
          customer = Customer.objects.get(user = user)
          order,created=Order.objects.get_or_create(customer=customer)
          items=order.orderitem_set.all()
          cartItems=order.get_cart_items
          if request.method == "POST":
               name =request.POST['name']
               email =request.POST['email']
               adress =request.POST['adress']
               state =request.POST['state']
               zipcode =request.POST['zipcode']
               country =request.POST['country']
               mahsulot= ''
               for item in items:
                    summa = item.product.cost * item.quantity
                    mahsulot += f"{item.product.name} - {item.product.cost} - x{item.quantity} - {summa}\n" 
               text = f"Xarid malumotlar:\n"\
                      f"{mahsulot}\n"\
                      f"Jami mahsulotlar - {cartItems}\n"\
                      f"Jami xarajat : {order.get_cart_total}\n"\
                      f"Xaridor nomi : {name}\n"\
                      f"Xaridor email : {email}\n"\
                      f"Xaridor manzili : {adress}\n"\
                      f"Xaridor davlati : {country}\n"
               url = f"https://api.telegram.org/bot5392920533:AAGAaS_fVLu-gJwCu8Em2HM64aFKlbqVLPo/sendMessage?chat_id=5332814623&text={text}"
               import requests
               requests.get(url)
               return redirect('/checkout')

               
     else:
          items=[]
          order={'get_cart_items':0}
          cartItems=order['get_cart_items']
     if Customer.objects.filter(user_id=request.user.id).exists():
          customer=Customer.objects.get(user_id=request.user.id)
          context={'items':items,'order':order,'cartItems':cartItems,'customer':customer}
     else:
        context={'items':items,'order':order,'cartItems':cartItems}
     return render(request,'checkout.html',context=context)
def loginPage(request):
     if request.user.is_authenticated:
             return redirect('/')
     if request.method == 'POST':
          name = request.POST['name']
          psw = request.POST['psw']
          user = authenticate(request, username=name, password=psw)
          if user is not None:
                login(request,user)
                return redirect('/')
          else:
               messages.error(request,"Username yoki parol xato")
               return redirect('/login')
             
     return render(request,'login.html',{'cartItems':0})

def register(request):
     if request.user.is_authenticated:
             return redirect('/')
     if request.method == 'POST':
          name = request.POST['name']
          psw = request.POST['psw']
          psw2 = request.POST['psw2']
          if User.objects.filter(username = name).exists():
               messages.error(request,"Bu Username bilan allaqachon ro'yxatdan o'tilgan")
               return redirect('/register')
          if psw != psw2 :
               messages.error(request,"Parollar har xil")
               return redirect('/register')
          User.objects.create_user(username = name,password = psw)
          return redirect('/login')
     
     return render(request,'register.html',{'cartItems':0})
def logoutUser(request):
     logout(request)
     return redirect('/login')
def update(request):
    import json
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
#     print(productId,action)
    user=request.user
    customer = Customer.objects.get(user = user)
    
    product=Products.objects.get(id=productId)
#     print(customer,product)
    order,created=Order.objects.get_or_create(customer=customer)
    print(f"#####################{order}##################{product}")
    orderitem,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderitem.quantity=(orderitem.quantity+1)
    elif action=='remove':
        orderitem.quantity=(orderitem.quantity-1)
    orderitem.save()
    if orderitem.quantity <=0:
        orderitem.delete()
    return JsonResponse('Mahsulot qoshildi',safe=False)