from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    rest_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    prod_code = models.IntegerField(default=100)
    added_by = models.CharField(max_length=50, default='user')
    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(max_length=500, default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque nisi a adipisci sapiente culpa, ipsum quos et facilis? Obcaecati doloremque sit non facilis molestiae eaque necessitatibus dolorem exercitationem saepe corrupti?')
    item_price=models.IntegerField()
    item_image=models.CharField(
        default='https://assets.materialup.com/uploads/b03b23aa-aa69-4657-aa5e-fa5fef2c76e8/preview.png',
        max_length=500
    )


    def __str__(self):
        return self.item_name




      