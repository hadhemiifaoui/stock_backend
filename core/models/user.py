from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from core.models import Role

class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **extra_fields):
        if not user_name:
            raise ValueError("user_name not valid")
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('the superuser must have the attribute is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('the superuser must have the attribute is_superuser=True')

        return self.create_user(user_name, password, **extra_fields)

    def get_by_natural_key(self, user_name):
        return self.get(user_name=user_name)



class User(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = []

    def has_permission(self, permission_key):
        if self.role and self.role.permissions:
            return self.role.permissions.get(permission_key, False)
        return False

    def __str__(self):
        return f"{self.user_name} ({'Active' if self.is_active else 'Inactive'})"
