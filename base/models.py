from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class User(AbstractUser):
    account = models.CharField(max_length=120,unique=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)
    address = models.CharField(max_length=200,null=True)
    avatar = models.ImageField(null=True,default='avatars/')

    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = ["username"]

    def create_superuser(self, account, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # 注意，这里我们不需要调用父类的 create_user 方法，因为 AbstractUser 没有 create_superuser
        # 我们直接使用 create 方法并传递所需的字段
        if not account:
            raise ValueError(_('The given account must be set'))
        if not password:
            raise ValueError(_('The given password must be set'))

        user = self._default_manager.create(account=account, password=password, **extra_fields)
        user.save(using=self._db)
        return user

class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    host = models.ForeignKey(User,on_delete=models.CASCADE)

