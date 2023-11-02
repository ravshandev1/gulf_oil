from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='menus')

    def __str__(self):
        return self.name


class Item(models.Model):
    menu = models.ForeignKey(Menu, models.CASCADE, related_name='items')
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='items')

    def __str__(self):
        return self.name
