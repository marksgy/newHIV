from django.db import models

# Create your models here.
class SessionInfo(models.Model):

    rd3 = models.StringField(max_length=50)
    state = models.StringField(max_length=50)
    session_key = models.StringField(max_length=50)
    openid = models.StringField(max_length=50)

    def __str__(self):
        return self._id

class UserInfo(models.Model):

    id = models.StringField(max_length=50)
    nickName = models.StringField(max_length=50)
    gender = models.StringField(max_length=50)
    language = models.StringField(max_length=50)
    city = models.StringField(max_length=50)
    province = models.StringField(max_length=50)
    country = models.StringField(max_length=50)
    vatarUrl = models.StringField(max_length=50)

    def __str__(self):
        return self.id

class OrderInfo(models.Model):
    time = models.StringField(max_length=50)
    place = models.StringField(max_length=50)
    methods = models.StringField(max_length=50)
    rd3 = models.StringField(max_length=50)

    def __str__(self):
        return self.id