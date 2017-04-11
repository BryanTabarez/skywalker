from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, UserManager,
    PermissionsMixin)
from django.db import models


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Standard fields
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)

    # Additionar fields: address, date_of_birth, cellphone, dni, phone
    address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cellphone = models.PositiveIntegerField(blank=True, null=True)
    dni = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email


class Employee(models.Model):
    ADMINISTRATOR = 'AD'
    EMPLOYEE = 'EM'

    EMPLOYEE_TYPE_CHOICES = (
        (ADMINISTRATOR, 'Administrator'),
        (EMPLOYEE, 'Employee'),
    )

    salary = models.PositiveIntegerField(null=True)
    employee_type = models.CharField(
        max_length=2,
        choices=EMPLOYEE_TYPE_CHOICES,
        default=EMPLOYEE,
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'