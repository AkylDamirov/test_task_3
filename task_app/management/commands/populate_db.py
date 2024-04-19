from django.core.management.base import BaseCommand
from task_app.models import Payment, Collect
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with mock data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Collect model
        for i in range(1000):
            author = User.objects.order_by('?').first()
            name = fake.word()
            occasion = fake.word()
            description = fake.text()
            current_amount = random.randint(100, 1000)
            image = 'test_task_3/covers/640px-Mark_Zuckerberg_F8_2018_Keynote.jpeg'
            date_finish = fake.future_date(end_date='+30d')
            FIO = fake.name()
            Collect.objects.create(author=author, name=name, occasion=occasion,
                                    description=description, current_amount=current_amount,
                                    image=image, date_finish=date_finish, FIO=FIO)

        # Payment model
        for i in range(1000):
            amount = random.randint(10, 100)
            user = User.objects.order_by('?').first()
            collect = Collect.objects.order_by('?').first()
            FIO = fake.name()
            Payment.objects.create(amount=amount, user=user, collect=collect, FIO=FIO)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock data'))