from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware that redirects requests from unauthenticated users to the sign-up page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URLs that do not require authentication
        exempt_urls = [
            reverse('app:sign_up'),
            reverse('app:sign_up.save'),
            reverse('app:sign_in'),
            reverse('app:sign_in.auth'),
            reverse('app:site'),

        ]

        # Check if the user is authenticated or if the request path is in the exempt list
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('app:sign_in')
        
        try:
            response = self.get_response(request)
        except Exception:
            # 例外が発生した場合に 'app:error_page' へリダイレクト
            return redirect('app:top')

        return response
