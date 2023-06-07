from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    SUPPORT = 1
    SALE = 2
    
    ROLES = (
        (SUPPORT, "support"),
        (SALE, "SALE"),
    )
    is_active = models.BooleanField(default=True)
    role  =  models.SmallIntegerField(choices=ROLES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    

