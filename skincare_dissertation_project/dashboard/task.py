from datetime import date
from django.contrib.auth import get_user_model
from .models import DailyLogin
from .utils import send_push_notification

User = get_user_model()

def send_daily_reminders():
    today = date.today()

    for user in User.objects.all():
        logged_in = DailyLogin.objects.filter(
            user=user,
            date=today
        ).exists()

        if not logged_in:
            send_push_notification(user)