from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, User
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=100, null=False)
#     phone = models.CharField(max_length=10, null=False)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100, null=False)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
    
#     groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'phone']
    
#     objects = MyUserManager()

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_admin(self):
#         return self.is_staff


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ManyToManyField(User)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    answer_text = models.CharField(max_length=500)
    question = models.ManyToManyField(Question)
    user = models.ManyToManyField(User)
    ans_date = models.DateTimeField('date published', null=True)

    def was_answered_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.answer_text
