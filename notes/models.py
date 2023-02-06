from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name='notes')
