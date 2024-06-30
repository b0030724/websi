from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
