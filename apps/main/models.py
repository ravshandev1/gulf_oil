from django.db import models
from django.core.files.storage import default_storage


class Menu(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='menus')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)


class Item(models.Model):
    menu = models.ForeignKey(Menu, models.CASCADE, related_name='items')
    name = models.CharField(max_length=250)
    pdf = models.FileField(upload_to='items')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        default_storage.delete(self.pdf.name)
        super().delete(*args, **kwargs)


class Country(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class ContactPublic(models.Model):
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField()
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.phone


class Contact(models.Model):
    country = models.ManyToManyField(Country, related_name='contacts')
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    staff = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    country_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.staff

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.country_count = self.country.count()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-country_count']


class Advertising(models.Model):
    image = models.FileField(upload_to='advertising')

    def __str__(self):
        return self.image.name

    def delete(self, *args, **kwargs):
        default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)
