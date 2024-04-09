from django.db import models


class MyModel(models.Model):
    data = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
