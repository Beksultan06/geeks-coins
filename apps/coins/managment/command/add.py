from django.core.management.base import BaseCommand
from apps.users.models import User
class Command(BaseCommand):
    help = "начисляем монеты всем пользователям"
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            user.profile.balance +=4
            user.profile.save()
        self.stdout.write(self.style.SUCCESS('монеты начислены успешно всем пользователям'))
