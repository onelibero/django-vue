from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import Model


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, permission=0, *extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.set_permission(permission)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    last_login = None  # 添加这行代码
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=50, unique=True)
    permission = models.CharField(max_length=12)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_id']

    objects = CustomUserManager()

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%s:%d" % (self.id, self.username, self.password, self.permission)

    # 自定义对应表名
    class Meta:
        db_table = "login"


class Comic(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    comicName = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    cover = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    label = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    remark = models.CharField(max_length=120)
    year = models.CharField(max_length=120)
    updateTime = models.CharField(max_length=120)
    number = models.IntegerField(max_length=120)
    popularity = models.IntegerField(max_length=120)
    url = models.CharField(max_length=120)

    class Meta:
        db_table = "comic"
