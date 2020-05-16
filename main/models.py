from django.db import models

# Create your models here.
class EmailSent(models.Model):
    mail_sender = models.CharField(max_length=50)
    mail_receipent = models.CharField(max_length=50)
    message = models.TextField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
