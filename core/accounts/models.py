from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
from core.accounts.manager import UserManager
User = get_user_model()
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100,unique=True)
    user_bio  = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD = 'phone_number' 
    REQUIRED_FIELDS = []
    objects = UserManager()