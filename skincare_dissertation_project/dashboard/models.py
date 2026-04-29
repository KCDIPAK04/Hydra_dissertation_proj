from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Model to track daily login activity
class DailyLogin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')


# Model to make phone alert system
User = get_user_model()

class DeviceToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField()








