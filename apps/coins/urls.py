from django.urls import path

from .views import TransferCoinsView, BurnCoinsView, TransactionHistoryView

urlpatterns = [
    path('transfercoins/', TransferCoinsView.as_view(), name = 'transfercoins' ),
    path('burncoins/', BurnCoinsView.as_view(), name= 'BurnCoins' ),
    path('TransactionHistory', TransactionHistoryView.as_view(), name='TransactionHistory')
]