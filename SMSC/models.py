from django.db import models
from django.core.validators import RegexValidator



# Create your models here.
# Модель для Абонент
class Abonent (models.Model):
    id = models.Index
    AbonentNumber = models.CharField(max_length=12)
    AbonentOrg = models.CharField(max_length=30)
    AbonentOperator = models.CharField(max_length=12)

class Account (models.Model):
    AccLogin = models.CharField(max_length=15)
    AccName = models.CharField(max_length=15)
    AccOrg = models.CharField(max_length=30)
    AccMail = models.CharField(max_length=30)
    AccSubscribe = models.CharField(max_length=12)

class CellNumbers(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return self.phone_number


class UploadFile(models.Model):
    description=models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media')
    uploadTime=models.DateTimeField(auto_now_add=True)
