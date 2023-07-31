from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=120,unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

class Stories(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)    
    title = models.CharField(max_length=30, null=False)
    tags = models.CharField(max_length=10, null=False)
    created_at = models.DateField(auto_now_add=True)
    story = models.TextField(null=False)
    image = CloudinaryField('image', default='')


    def __str__(self):
        return self.title





