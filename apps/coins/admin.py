from django.contrib import admin

# Register your models here.
from .models import Coins
@admin.register(Coins)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'history_of_transactions']

