from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class MyUserManager(BaseUserManager):
    def create_user(self,name,last_name,document_number,phone,email,address,gender,type,password=None):
        if not name:
            raise not name('Must have a name')
        if not last_name:
            raise not last_name('Must have a last name')
        if not document_number:
            raise not document_number('Must have a document number')
        if not phone:
            raise not phone('Must have a phone number')
        if not email:
            raise not email('Must have an email')
        if not address:
            raise not address('Must have an address')
        if not gender:
            raise not gender('Must select a gender')
        if not type:
            raise not type('Must select an user type')
        user = self.model(

            name=name,
            last_name = last_name,
            document_number=document_number,
            phone=phone,
            email=self.normalize_email(email),
            address=address,
            gender=gender,
            type=type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,last_name,document_number,phone,email,address,gender,type,password):
        user = self.create_user(
            name=name,
            last_name=last_name,
            document_number=document_number,
            phone=phone,
            email=email,
            address=address,
            gender=gender,
            type=type,
            password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    TYPE_ADMIN = 1
    TYPE_CLIENT = 2
    TYPE_EMPLOYEE = 3
    TYPE_CHOICES = ((TYPE_ADMIN, 1), (TYPE_CLIENT, 2), (TYPE_EMPLOYEE, 3))
    FEMALE = "femenino"
    MASCULINE = "masculino"
    DWTS = "prefiero_no_decirlo"
    OTHERG = "otro"
    TYPE_GENDER = ((FEMALE, "Femenino"), (MASCULINE, "Masculino"), (DWTS, "Prefiero_no_decirlo"), (OTHERG, "Otro"))

    OnlyLetters = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters.')

    name = models.TextField(max_length=50, validators=[OnlyLetters])
    last_name = models.TextField(max_length=50, validators=[OnlyLetters])
    document_number = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=200,unique=True)
    password = models.TextField(max_length=250)
    address = models.TextField(max_length=50)
    gender = models.CharField(max_length=19, choices=TYPE_GENDER)
    type = models.IntegerField(choices=TYPE_CHOICES)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name','last_name','document_number','phone','address','gender','type']

    objects = MyUserManager()

    def _str_(self):
        return self.email
    def has_perm(self,perm, obj=None):
        return self.is_staff
    def has_module_perms(self,app_label):
        return True
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)