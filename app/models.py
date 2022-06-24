from django.db import models

# Create your models here.
class UserType(models.Model):
    type = models.CharField(max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=2,default='U')
    point = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    head_portrait = models.CharField(max_length=64,default='123123')
    juris = models.ForeignKey('UserType',on_delete=models.CASCADE)

class Article_Path(models.Model):
    title = models.CharField(max_length=32)
    path = models.CharField(max_length=64)
    classes = models.CharField(max_length=16)


#一下没用，是为了防止上个版本暴毙
class article(models.Model):
    title = models.CharField(max_length=32)
    path = models.CharField(max_length=64)
    classes = models.CharField(max_length=16)

class user(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=2)
    point = models.IntegerField()
    status = models.IntegerField()
    head_portrait = models.CharField(max_length=64)
    juris = models.ForeignKey('UserType',on_delete=models.CASCADE)

