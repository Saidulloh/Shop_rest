from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
    getter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='getter')        
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('timestamp',)