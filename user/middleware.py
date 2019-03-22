from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class FilterMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path != '/user/login':
            print(request.path)
            if request.user.is_authenticated:
                pass
            else:
                # reverse直接根据名字跳转
                return HttpResponseRedirect(reverse('login'))
