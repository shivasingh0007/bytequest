from django.db import models

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
       return self.name


class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()
    product_qty=models.IntegerField()
    product_image=models.ImageField(upload_to='uploads/')

    def __str__(self):
       return self.category
