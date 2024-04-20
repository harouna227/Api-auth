from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


""" Personnalisation du model user en utilisant **extra_fields """
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email valide.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user doit avoir is_staff = True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super user doit avoir is_superuser = True")
        
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=50, unique = True)
    first_name = models.CharField(max_length=50, unique = True)
    last_name = models.CharField(max_length=50, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    objects = UserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return f"{self.first_name} | {self.email}"


""" Une deuxième façcon de parsonnaliser le model user"""
# class UserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password=None):
#         if not self.email:
#             raise ValueError("L'utilisateur doit avoir un email valide.")
        
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, first_name, last_name, password=None):
#         user = self.create_superuser(
#             email=email,
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             password=password
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         unique=True,
#         max_length=255,
#         verbose_name="Adresse mail"
#     )
#     username = models.CharField(max_length=60, unique=True)
#     first_name = models.CharField(max_length=100, unique=True)
#     last_name = models.CharField(max_length=100, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_supperuser = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD  = "email"
#     REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

#     def __str__(self):
#         return f"{self.first_name} - {self.email}"
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def has_perm(self, perm, obj=None):
#         "L'utilisateur dispose-t-il d'une autorisation spécifique ?"
#         # Réponse la plus simple possible : Oui, toujours
#         return True

#     def has_module_perms(self, app_label):
#         "L'utilisateur a-t-il les autorisations nécessaires pour afficher l'application « app_label » ?"
#         # Réponse la plus simple possible : Oui, toujours
#         return True
    