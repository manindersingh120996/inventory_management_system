from email.headerregistry import Address
import profile
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser
from base.models import BaseModel
from django.core.validators import RegexValidator
# Create your models here.
     

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email = models.CharField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=400,null=True,blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^[6-9]\d{9}$")
    contact = models.CharField(validators=[phoneNumberRegex],max_length=10,unique=True)
    profile_image = models.ImageField(upload_to = 'profile')
    
