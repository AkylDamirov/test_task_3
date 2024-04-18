from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collect = models.ForeignKey('Collect', on_delete=models.CASCADE)
    FIO = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user-{self.user}, amount-{self.amount}'

class Collect(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)
    description = models.TextField()
    amount_to_achieve = models.CharField(max_length=100, default='Infinitive')
    current_amount = models.IntegerField()
    # amount_donations = models.IntegerField()
    image = models.ImageField(upload_to='covers/')
    date_finish = models.DateTimeField()
    when_created = models.DateTimeField(auto_now_add=True)
    FIO = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def donations(self):
        return Collect.objects.filter(collect=self)

    @property
    def amount_donations(self):
        return self.payment_set.count()

    class Meta:
        verbose_name = 'Collect'
        verbose_name_plural = 'Collects'




