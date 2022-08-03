from django.http import request
from django.shortcuts import render
from django.views.generic import View
from django.middleware.csrf import get_token
from django.conf import settings
import datetime

def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow(
    ) + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires,
                        domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)


class IndexView(View):
    def get(self,request):
        response = render(request,'index.html')
        set_cookie(response,"csrftoken",get_token(request))
        return response