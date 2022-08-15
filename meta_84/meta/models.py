from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to='media')

    def __str__(self):
        return self.user.username
