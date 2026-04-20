from django.shortcuts import redirect
from .utils import is_profile_complete

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            allowed_paths = [
                '/accounts/complete-profile/',
                '/accounts/login/',
                '/accounts/signup/',
                '/admin/',
            ]

            if not any(request.path.startswith(p) for p in allowed_paths):

                if not is_profile_complete(request.user):
                    return redirect('complete_profile')

        return self.get_response(request)