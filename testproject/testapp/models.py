from django.db import models


class TestModel(models.Model):
    char_field = models.CharField(max_length=30)
    integer_field = models.IntegerField()
    date_field = models.DateField()
