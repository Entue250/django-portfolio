from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    reason = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.reason}"