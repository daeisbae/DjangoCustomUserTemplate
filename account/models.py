from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
# Description: Choice between superuser and normal user
# Precondition: using django createsuperuser, create_superuser() function is being used. Else, create_user() function is being used.
# Postcondition: None
class AccountManager(BaseUserManager):
    use_in_migrations = True

    # Creating User And Fill Information
    def _create_user(self, email, name, phone, password, **extra_fields):
        values = [email, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Set user as normal user
    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    # Set user as superuser
    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)

# Description: Custom User Authentication Model
# Preconditions: None
# Postconditions: User can have email, name, phone, password with a unique name field

# PermissionsMixin is a class that provides a set of default permissions to be used with Django's permission system.
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'phone']

    def get_full_name(self):
        return self.name