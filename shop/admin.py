from django.contrib import admin
from .models import Item, Transaction, Reviews, Purchaser,TransactionItem, Cart

admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Reviews)
admin.site.register(Purchaser)
admin.site.register(TransactionItem)
admin.site.register(Cart)
