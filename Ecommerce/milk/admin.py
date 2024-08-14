from django.contrib import admin
# Register your models here.
from .models import*

@admin.register(Product)
class ProductmodelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price','product_image', 'discounted_price', 'category']   


@admin.register(Customer)
class CustomermodelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']   

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','products','quantity']

@admin.register(Payments)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(Orderplaced)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customers','product','quantity','ordered_date','ordered_date','status','payments']



