from .models import CustomUser

def is_profile_complete(user):
    return user.email and user.username