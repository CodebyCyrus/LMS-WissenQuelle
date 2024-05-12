from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email= models.EmailField(unique=True)
    full_name = models.CharField(unique=True, max_length=100)
    otp = models.CharField(unique=True, max_length=100)

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

def __str__(self):
    return self.email

def save(self, *args, **kwargs):
    email_username, full_name = self.email.spilit("@") #codebycyrus@gmail.com so its grab everything before @
    if self.full_name == "" or self.full_name == None:
        self.full_name == email_username
        if self.username == "" or self.username == None:
            self.username = email_username
            super(User, self).save("*args, **kwargs")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="user_folder", default="defualt-user.jpg", null=True, blank=True)
    full_name = models.CharField( max_length=100)
    country = models.CharField( max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    if self.full_name:
      return str(self.full_name) 
    else:
        return str(self.user.full_name)


def save(self, *args, **kwargs):
    if self.full_name == "" or self.full_name == None:
        self.full_name == self.user.username
        
    super(Profile, self).save("*args, **kwargs")