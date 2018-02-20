from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_messages')
    to_user = models.ForeignKey(User, related_name='recieved_messages')
    text = models.CharField(max_length=2000)
    created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-created',)

        
