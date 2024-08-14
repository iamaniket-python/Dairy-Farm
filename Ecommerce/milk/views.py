from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Count
from django.views import View
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib import messages
from . forms import CustomerProfileForm,CustomerRegistrationForm
from . models import Cart, Customer,  Product ,Orderplaced


# Create your views here.
def Home(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,'main/home.html',locals())

def about(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,'main/about.html',locals())
def contact(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,'main/contact.html',locals())

class CutomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request,'main/CustomerRegistration.html',locals())
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request,"congratulations ! user Register Successful ")
        else:
            messages.warning(request,"Invalid Please Try again")
        return render(request,'main/CustomerRegistration.html',locals())
    


class Categoryview(View):
    def get(self,request,val):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        product =Product.objects.filter(category=val)
        title = Product.objects.filter(category=val)
        return render(request,'main/category.html',locals())

class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=product.objects.filter(category=product[0].category).values('title')
        return render(request,'main/category.html',locals())



class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"main/productdetails.html",locals())


class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,"main/profile.html",locals())

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']

            req= Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            req.save()
            messages.success(request,'Badhaai ho aap enter ho chuke hai')

        else:
            messages.warning(request,'Invalid please try again')
        return render(request,"main/profile.html",locals())

def address(request):
    add =Customer.objects.filter(user=request.user)
    return render(request,"main/address.html",locals())

class updateAddress(View):
    def get(self,request,pk):
       add =Customer.objects.get(pk=pk)
       form =CustomerProfileForm(instance=add)
       return render(request,'main/updateAddress.html',locals())
    def post(self,request,pk):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            add =Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.mobile=form.cleaned_data['mobile']
            add.save()
            messages.success(request,'Address updated successfully')
            return redirect('address')
        else:
            messages.warning(request,'Invalid please try again')
            
        return render(request,'main/updateAddress.html',locals())
    

def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    product =Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.discounted_price
        amount=amount+value
    totalamount=amount + 40
    
    return render(request,'main/addtocart.html',locals())

def checkout(View):
    def get(self,request):
        user =request.user
        add=Customer.objects.filter(user=user)
        cart= items=Cart.objects.filter(user=user)
        famount= 0
        for p in cart:
            value =p.quantity * p.product.discounted_price
            famount =famount + value
        totalamount= famount + 40
        totalamount =int(totalamount * 100)
        client =razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data={
            'amount': razoramount,'currency':'INR','receipt':'order_reptid_12' # type: ignore
        }
        payment_resposnse = client.order.create(data=data)
        order_id = payment_resposnse['id']
        order_status = payment_resposnse['status']
        if order_status == 'created':
            payment= Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()
        return render(request,'main/checkout.html',locals())

def plus_cart(request):
    if request.method =="GET":
        prod_id=request.GET["prod_id"]
        c.quantity+=1
        c.save()
        user =request.user
        cart =Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value =p.quantity * p.product.discounted_price
            amount =amount + value
        totalamount= amount + 40
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method =="GET":
        prod_id=request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user =request.user
        cart =Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value =p.quantity * p.product.discounted_price
            amount =amount + value
        totalamount= amount + 40
    

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method =="GET":
        prod_id=request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()     
        user =request.user
        cart =Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value =p.quantity * p.product.discounted_price
            amount =amount + value
        totalamount= amount + 40
       
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def orders(request):
    order_placed=Orderplaced.objects.filter(user=request.user)
    return render(request,'main/orders.html',locals())

def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    user =request.user
    customer=Customer.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid =True
    payment.razorpay_payment_id = payment_id
    payment.save()
    # to save order details
    cart=Cart.objects.filter(user=user)
    for c in cart:
        Orderplaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()

    return redirect('orders')