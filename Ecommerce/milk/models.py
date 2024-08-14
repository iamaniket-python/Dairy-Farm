from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGEORY_CHOICES=(
    ('Milk','Milk'),
    ('Curd','Curd'),
    ('Ghee','Ghee'),
    ('Paneer','Paneer'),
    ('Chesse','Chesse'),
    ('Ice-Cream','Ice-Cream'),
    ('Milkshake','Milkshake'),
    ('Lassi','Lassi'),
)
STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Karnataka','Karnataka'),
    ('Tamilnadu','Tamilnadu'),
    ('Telangana','Telangana'),
    ('Maharashtra','Maharashtra'),
    ('West Bengal','West Bengal'),
    ('Rajasthan','Rajasthan'),
    ('Gujarat','Gujarat'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Punjab','Punjab'),
    ('Jharkhand','Jharkhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Haryana','Haryana'),
    ('Delhi','Delhi'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Sikkim','Sikkim'),
    ('Kerala','Kerala'),
    ('Uttarakhand','Uttarakhand'),
    ('Other','Other'),
)
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
class Product(models.Model):
    title = models.CharField(max_length=120)
    selling_price =models.FloatField()
    discounted_price=models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp=models.TextField(default='')
    category =models.CharField(choices=CATEGEORY_CHOICES,max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    product_image= models.ImageField(upload_to='product')


    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField()
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

class Orderplaced(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    customers= models.ForeignKey(Customer,on_delete=models.CASCADE)
    products= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveBigIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    Payments =models.ForeignKey(Payments,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
# class Payment(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     amount =models.FloatField()
#     razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
#     razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
#     paid =models.BooleanField(default=False)
