from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='menus')

    def __str__(self):
        return self.name


class Item(models.Model):
    menu = models.ForeignKey(Menu, models.CASCADE, related_name='items')
    name = models.CharField(max_length=250)
    pdf = models.FileField(upload_to='items')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class ContactPublic(models.Model):
    address = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.phone


class Contact(models.Model):
    country = models.ForeignKey(Country, models.CASCADE, related_name='contacts')
    address = models.TextField()
    email = models.EmailField()
    staff = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.staff
