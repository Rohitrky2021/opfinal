from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator


STATE_CHOICES=(
   #tuple form me 
    ('ANDHRA.PRADESH','ANDHRA.PRADESH'),
    ('ARUNACHAL PRADESH','ARUNACHAL PRADESH'),
    ('ASSAM','ASSAM'),
    ('BIHAR','BIHAR'),
    ('JHARKHAND','JHARKHAND'),
    ('GOA','GOA'),
    ('GUJRAT','GUJRAT'),
    ('HARYANA','HARYANA'),
    ('HIMACHALPRADESH','HIMACHALPRADESH'),
    ('KARNATAKA','KARNATAKA'),
    ('KERALA','KERALA'),
    ('MADHYA PRADESH ','MADHYA PRADESH '),
    ('MAHARASHTRA','MAHARASHTRA'),
    ('NAGALAND','NAGALAND'),
    ('UTTAR PRADESH','UTTAR PRADESH'),
    ('WEST BENGAL','WEST BENGAL'),

)
#many to one relation from user 
#down m hur model m ek id generate hoga
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)


    def __str__(self):
     return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
    ('Mo','Mo'),
    ('ban','ban')
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    product_image =models.ImageField(upload_to='producting')


    def __str__(self):
     return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveBigIntegerField(default=1)
    

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


    def __str__(self):
     return str(self.id)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)     

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity =models.PositiveBigIntegerField(default=1) 
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,
    choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
     return str(self.id)
     