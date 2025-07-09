from django.db import models

# Create your models here.
class classtype(models.Model):
    questions=models.IntegerField(unique=True),
    type_questions=models.IntegerField(unique=True)