from django.db import models
from django.contrib.auth.models import User





#  Profile model view
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=200 , default='users')

    def __str__(self):
        return self.user.username



