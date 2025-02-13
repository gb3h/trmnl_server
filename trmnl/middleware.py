from asyncio import iscoroutinefunction
from functools import wraps

from django.http import JsonResponse

from .models import APIKey


class ApiKeyAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not getattr(view_func, "require_api_key", False):
            return

        api_key = request.headers.get("Authorization", None)
        if not api_key:
            return self.reject

        # Parse Bearer token out
        if api_key.startswith("Bearer "):
            api_key = api_key.split("Bearer ")[1]

        # Check if the API key is valid
        api_key = APIKey.objects.filter(key=api_key).first()
        if not api_key:
            return self.reject

        # Attach the API key to the request
        request.api_key = api_key
        return

    @property
    def reject(self):
        return JsonResponse({"status": 403, "message": "Invalid API Key"}, status=403)


def require_api_key(view_func):
    """Mark a view function as requiring an API key."""

    if iscoroutinefunction(view_func):

        async def _view_wrapper(request, *args, **kwargs):
            return await view_func(request, *args, **kwargs)

    else:

        def _view_wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)

    _view_wrapper.require_api_key = True

    return wraps(view_func)(_view_wrapper)
