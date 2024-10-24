from django.core.management.base import BaseCommand
from apps.users.models import User
class Command(BaseCommand):
    help = "отнимаем монеты"
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            user.profile.balance = 0
            user.profile.save()
        self.stdout.write(self.style.SUCCESS('не испоьзованные монеты успешно сгорели '))
