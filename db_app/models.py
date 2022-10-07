from django.db import models

# Create your models here.
class Geo(models.Model):
    lat = models.FloatField(max_length = 10)
    lng = models.FloatField(max_length = 10)

    def __str__(self):
        return str(self.lat) + ", " + str(self.lng)

class Address(models.Model):
    street = models.CharField(max_length = 250)
    suite =  models.CharField(max_length = 250)
    city = models.CharField(max_length = 250)
    zipcode = models.CharField(max_length = 250)
    geo = models.ForeignKey(Geo, on_delete = models.CASCADE)

    def __str__(self):
        return self.city

class Company(models.Model):
    name = models.CharField(max_length = 250)
    catchPhrase = models.TextField()
    bs = models.TextField()

    def __str__(self):
        return self.name

class Users(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 250)
    username = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    phone = models.CharField(max_length = 30)
    website = models.CharField(max_length = 250)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.name