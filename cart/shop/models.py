import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Item(models.Model):
    item_name = models.CharField(default="Item", max_length=50)
    description = models.CharField(default="Detail", max_length=500)
    warranty_duration = models.IntegerField(default=1)
    price = models.FloatField(default=0.00)
    publish_date = models.DateTimeField("date published")
    def __str__(self):
    	return self.item_name
    def __str__(self):
    	return str(self.id)

class Purchaser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name
 
class Transaction(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity_of_item = models.IntegerField(default=1)	
	discount = models.FloatField(default=0.0)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=50)
	purchase_date = models.DateTimeField(auto_now_add=True)
	total_price = models.FloatField(default=1.0)
	amount_discount = models.FloatField(default=1.0)
	status = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)
	def was_purchased_recently(self):
		return self.purchase_date >= timezone.now() - datetime.timedelta(days=1)
	@property
	def foo(self):
		return self.item.price * self.quantity_of_item
	@property
	def amt_disc(self):
		return (self.item.price * self.quantity_of_item) * ((self.discount) *0.01)
	def save(self, *args, **kwargs):
		self.total_price = self.quantity_of_item * self.item.price 
		self.amount_discount = (self.item.price * self.quantity_of_item) * ((self.discount) *0.01)
		super(Transaction, self).save(*args, **kwargs)
	def __str__(self):
   	    return str(self.id)

class TransactionItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
	transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	transaction_item_status = models.BooleanField(default=False, null=True, blank=False)
	def __str__(self):
		return str(self.id)

class Cart(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.FloatField(default=1.00)
	cart_status = models.BooleanField(default=False, null=True, blank=False)
	cart_id = models.IntegerField(default=1)

	def __str__(self):
		return str(self.id)

class Reviews(models.Model):
	username = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	review = models.CharField(max_length=500)
	rating = models.IntegerField(default=5, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
	date_reviewed = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.rating)




