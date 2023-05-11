from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register_page, name="register_page"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="logout"),
    path("", views.welcome, name="welcome"),
    path("index/", views.index, name="index"),
    path("transactions/", views.transactions, name="transactions"),
    path("customers/", views.reviews, name="reviews"),
    path("cart/", views.cart, name="cart"),


    path("<str:item_name>/", views.detail, name="detail"),
    path("<int:item_id>/add_to_cart", views.add_to_cart, name="add_to_cart"),
]
