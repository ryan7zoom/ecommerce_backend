from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class DisableCSRFOnAPI(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/product/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
