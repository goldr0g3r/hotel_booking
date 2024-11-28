from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
import uuid
from django.conf import settings


# User Manager


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not given a valid email!")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, name: str, email: str, password: str, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(
        self,
        email: str | None,
        name: str | None,
        password: str | None,
        **extra_fields: Any,
    ) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="uploads/avatars", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = [
        "name",
    ]

    # rename the avatar file to the user id
    def save(self, *args, **kwargs):
        if self.avatar:
            self.avatar.name = f"{self.id}_avatar.png"
        super().save(*args, **kwargs)

    def get_avatar_url(self) -> str:
        if self.avatar:
            print(self.avatar.url)
            return f"{settings.WEBSITE_URL}{self.avatar.url}"
        return "https://www.gravatar.com/avatar/"
