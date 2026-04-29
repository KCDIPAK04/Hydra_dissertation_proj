from dashboard.models import DeviceToken
from firebase_admin import messaging


def send_push_notification(user):
    tokens = DeviceToken.objects.filter(user=user).values_list('token', flat=True)

    for token in tokens:
        message = messaging.Message(
            notification=messaging.Notification(
                title="Reminder 🔔",
                body="You didn't log in today 🔥",
            ),
            token=token,
        )

        response = messaging.send(message)
        print("Sent:", response)