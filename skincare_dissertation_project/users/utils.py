from .models import UserProfile

def is_profile_complete(user):
    profile, _ = UserProfile.objects.get_or_create(user=user)

    return bool(
        profile.age and
        profile.weight and
        profile.skin_type
    )