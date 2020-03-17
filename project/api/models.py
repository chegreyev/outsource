from django.db import models

# Create your models here.
class Employees(models.Model):
    telegram_id = models.IntegerField()

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    iin = models.IntegerField(max_length=12)
    udv_number = models.IntegerField(max_length=8)
    udv_place = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    bank_card = models.IntegerField(max_length=12)
    iban = models.CharField(max_length=20)

    contact_phone = models.CharField(max_length=20)
    email_address = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)

    def __str__(self):
        return self.telegram_id