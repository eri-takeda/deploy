from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

objects = models.Manager()
        

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    age = models.IntegerField()
    prefecture = models.CharField(max_length=100, blank=True, null=True)  # 追加
    address = models.CharField(max_length=255, blank=True, null=True)  # 追加
    user_type = models.CharField(max_length=50, blank=True, null=True)  # 追加
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')


#各テーブルの作成

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    prefecture = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    image = models.ImageField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    color = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=255)
    spayed = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recruiting(models.Model):
    recruiting_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)  
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MessageHistory(models.Model):
    message_id = models.AutoField(primary_key=True)
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


