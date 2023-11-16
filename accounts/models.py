from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Permission

class UserType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_completed', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    usn = models.CharField(max_length=100, unique=True,null=True,blank=True)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15,null=True,unique=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    course = models.CharField(max_length=255,null=True,blank=True)
    graduation_year = models.IntegerField(null=True,blank=True)
    abroad_year = models.IntegerField(null=True,blank=True)
    abroad_season = models.CharField(max_length=100,null=True,blank=True)
    is_completed = models.BooleanField(default=False)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
