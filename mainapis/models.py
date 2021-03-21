from django.db import models

# Create your models here.
import jsonfield

class Conversation(models.Model):
    sender = models.CharField(primary_key=True,max_length=15)
    message = models.CharField(null=True,max_length=1600)
    selections = jsonfield.JSONField()
    last_selection = models.CharField(null=True,max_length=200)
    language = models.CharField(null=True,max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
