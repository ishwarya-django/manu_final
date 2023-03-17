from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group





class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email,role,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            role=role,
       
        )
     
        user.is_active = True
      
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
   
        user.save(using=self._db)
        return user

ROLE_CHOICES = (
            ("Employee", "Employee"),
            ("Customer", "Customer"),
            ("Admin", "Admin"),
)

class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    group           = models.ForeignKey(Group,on_delete =models.CASCADE,null=True)
    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superadmin        = models.BooleanField(default=False)
    role            = models.CharField(choices=ROLE_CHOICES,max_length=70,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

new_group, created = Group.objects.get_or_create(name='admin')
new_group, created = Group.objects.get_or_create(name='staff')
new_group, created = Group.objects.get_or_create(name='user')
new_group, created = Group.objects.get_or_create(name='customer')
new_group, created = Group.objects.get_or_create(name='employee')


class Role_assign(models.Model):
    group           = models.ForeignKey(Group,on_delete =models.CASCADE,null=True)
    user           = models.ForeignKey(User,on_delete =models.CASCADE,null=True)

    class Meta:
         
        permissions = (
            ("staff", "staff"),
            ("admin", "admin"),
            ("user", "user"),
            ("customer", "customer"),
            ("employee", "employee"),
        )

