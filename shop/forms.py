from django.forms import ModelForm
from .models import Reviews, Transaction, Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class ReviewForm(ModelForm):
	class Meta:
		model = Reviews
		fields = ["item", "review", "rating"]

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = ["item", "quantity_of_item", "discount", "address"]

class AddToCartForm(ModelForm):
	class Meta:
		model = Cart 
		fields = ["item", "quantity", "username"]