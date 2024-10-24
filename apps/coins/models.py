from django.db import models

from apps.users.models import User

# Create your models here.
class Coins(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)
    sender = models.ForeignKey(User, verbose_name = "передача монет", on_delete=models.CASCADE,  related_name='sent_coins')
    history_of_transactions = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(User, verbose_name = "получатель монет", on_delete=models.CASCADE, related_name='received_coins')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="монеты"