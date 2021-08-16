from typing import ContextManager
from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(user,related_name="author_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_30_msg(self):
        return Message.objects.order_by('-timestamp').all()[:30]