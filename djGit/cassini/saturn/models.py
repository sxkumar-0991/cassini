from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User must enter a valid email.")
        email = self.normalize_email(email)
        customuser = self.model(email=email)
        customuser.set_password(password)
        customuser.save(using=self._db)
        return customuser

    def create_superuser(self,email,password):
        customuser = self.create_user(email=email,password=password)
        customuser.is_superuser = True
        customuser.save(using=self._db)
        return customuser

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('EMAIL_ID'), unique=True, max_length=255)
    is_superuser = models.BooleanField(_('User is Admin'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Member is Staff'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}--{}".format(self.title,self.artist)