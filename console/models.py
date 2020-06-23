from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=254)
    product_code = models.CharField(max_length=254)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=254)
    customer_code = models.CharField(max_length=254)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


class Module(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, default='Null', null=True)

    def __str__(self):
        return self.module_name


class Version(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.CharField(max_length=254)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    update_at = models.DateTimeField('date published', auto_now=True)
