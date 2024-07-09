from django.db import models

# Create your models here.

class promotions(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)


class collection(models.Model):
    title = models.CharField(max_length= 255)
    featured_products = models.ForeignKey('product', on_delete= models.SET_NULL, null=True, related_name ='+' )

class product(models.Model):
    sku = models.CharField(max_length=255, primary_key =True)
    slug = models.SlugField(default = '-')
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price  = models.DecimalField(max_digits=4, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #auto_now makes Django update everytinme
    #auto_now_add only updates it for first time 
    collection = models.ForeignKey(collection, on_delete= models.PROTECT)
    #for delete, we use PROTECT. This ensures that we don't end up deleting 
    #all the products in colleciton if we delete the collection

    promotions =  models.ManyToManyField(promotions)

class customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES= [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices= MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

    class Meta:
        db_table = 'customer'
        models.Index(fields=['last_name', 'first_name'])


class order(models.Model):

    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED = 'F'
    PAYMENT_STATUS = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_FAILED, 'Failed'),
        (STATUS_COMPLETE,'Complete')
    ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=STATUS_PENDING)
    customer = models.ForeignKey(customer, on_delete = models.PROTECT)
    #one customer can have multiple order 

class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(customer, on_delete = models.PROTECT, primary_key = True)
    zip_code = models.CharField(max_length=5, verbose_name="Zip Code",null=True)
    sip = models.CharField(max_length=255, default= 'sip')
    #never delete orders, use protect. Order shows your sales
    #Here address depends on customer, primary_key ensures that Django does not create new ID 
    #for different addresses. Hence, ensuring uniqueness.

class cart(models.Model):
    # customer = models.OneToOneField(customer, on_delete= models.CASCADE, primary_key=True)
    # cart_items = [] 
    # quantity = len(cart_items)
    created_at = models.DateTimeField(auto_now_add=True)

class order_item(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order =  models.ForeignKey(order, on_delete = models.PROTECT)
    product = models.ForeignKey(product, on_delete = models.PROTECT)

class cart_item(models.Model):
    cart = models.ForeignKey(cart, on_delete= models.CASCADE)
    product = models.ForeignKey(product,on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()




