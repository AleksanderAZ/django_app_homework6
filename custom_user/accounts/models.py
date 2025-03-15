from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        if not phone_number:
            raise ValueError('Phone_number field is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError('Superuser must have is staff=True.')
        if extra_fields.get("is_superuser") is not True:
            raise ValueError('Superuser must have is is_superuser=True.')
        
        return self.create_user(email, phone_number, password, **extra_fields)
    
    def active_users_after_date(self, date):
        return self.filter(is_active=True, date_joined__gte=date)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Пошта')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Телефон')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Ім`я')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Прізвище')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='День  народження')
    profile_picture = models.ImageField(upload_to='profile_picts/', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    is_staff = models.BooleanField(default=True, verbose_name='Персонал')
    date_joined = models.DateField(default=timezone.now, verbose_name='Дата реєстрації')
    preferred_language = models.CharField(max_length=10, choices=[
        ('uk', 'Українська'),
        ('en', 'English')
    ], default='uk', verbose_name='Мова')
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        permissions = [
            ('can_view_profiles', 'Переглядати профілі інших'),
            ('can_edit_profiles', 'Редагувати профілі інших'),
        ]
    
    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

