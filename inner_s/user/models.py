from django.db import models

from django.contrib.auth import get_user_model


User_t = get_user_model()


class User(models.Model):
    id = models.IntegerField('id', primary_key=True)
    login = models.CharField('login', max_length=150)
    password = models.CharField('password', max_length=150)
    acs_lvl = models.IntegerField('acs_lvl')

    def __str__(self):
        return self.id
