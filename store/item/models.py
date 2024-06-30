from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='item_profile', null=True, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=225)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories' 
        
    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    brand= models.CharField(max_length=225)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Item, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

