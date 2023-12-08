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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        self.country_count = self.country.count()
        super().save()

    class Meta:
        ordering = ['-country_count']


class Advertising(models.Model):
    image = models.FileField(upload_to='advertising')

    def __str__(self):
        return self.image.name
