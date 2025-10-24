from django.db import models
from django.conf import settings

class Ad(models.Model):
    """
    Модель объявления с заголовком, описанием и владельцем.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
