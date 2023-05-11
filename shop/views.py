from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Item, Transaction, Reviews, Purchaser,TransactionItem, Cart
from .forms import ReviewForm, CreateUserForm, AddToCartForm

# Displays the users reviews on the first page
def welcome(request):
	if request.user.is_authenticated:
		rev = Reviews.objects.filter(username=request.user).order_by('id')
	else:
		return redirect('index')
	context = {"rev":rev}
	return render(request, 'welcome.html', context)

# User sign up 
def register_page(request):
	if request.user.is_authenticated:
		messages.success(request, 'You are already are registered or logged in.')
		return redirect('welcome')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login_page')
		context = {'form':form}
		return render(request, 'register.html', context)

# User login
def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('welcome')
		else:
			messages.info(request, 'Username or password is incorrect')
	context = {}
	return render(request, 'login.html', context)
def logout_user(request):
	logout(request)
	return redirect('login_page')

# Leave review form
@login_required(login_url='login_page')
def reviews(request):
	form = ReviewForm(data=request.POST)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.username = request.user 
			form.save()
			messages.success(request, 'You successfuly left a review')
			return redirect('welcome')
		else:
			messages.info(request, 'Invalid review')
	context = {"form":form}
	return render(request, 'customers.html', context)

# Display items list
def index(request):
	try:
		latest_item_list = Item.objects.order_by('id')
	except Item.DoesNotExist:
		raise Http404("Item does not exist")
	template = loader.get_template("index.html")
	context = {
		"latest_item_list": latest_item_list,
	}
	return render(request, "index.html", context)

def detail(request, item_name):
  return render(request, "detail.html")

# Transactions page
@login_required(login_url='login_page')
def transactions(request):
	transaction_list = Transaction.objects.order_by('-id')
	template = loader.get_template("transactions.html")
	context = {
		"transaction_list": transaction_list,
	}
	return render(request, "transactions.html", context)

@login_required(login_url='login_page')
def cart(request):
	if request.user.is_authenticated:
		cart = Cart.objects.filter(username=request.user).order_by('id')
	else:
		return redirect('welcome')
	context = {"cart":cart,}
	return render(request, 'cart.html', context)

@login_required(login_url='login_page')
def add_to_cart(request, item_id):
	form = AddToCartForm(data=request.POST)
	if request.method == "POST":
		form = AddToCartForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Added item to your cart")
			return redirect('index')
	# item = get_object_or_404(Item, pk=item_id)
	# if request.user.is_authenticated:
	# 	cart, created = Cart.objects.get_or_create(username=request.user)
	# 	cart.item.save()
	else:
		print("Error adding to cart")
	context = {"cart":cart,"form":form,}
	# context = {"item":item, "cart":cart,"form":form,}
	return render(request, "add_to_cart.html", context)
	return redirect('cart')

