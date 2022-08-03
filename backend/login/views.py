from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from login.models import Usuario
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def csrfGet(request):
    token = get_token(request)
    return HttpResponse(token)

@method_decorator(csrf_exempt, name='dispatch')
class LogarView(View):
    def get(self,request):
        token = get_token(request)
        return HttpResponse(token)
    def post(self,request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            email = data['email']
            password= data['password']
            print(f'{email}, {password}')
            user =authenticate(email=email,password=password)
            if user is not None:
                usu = Usuario.objects.get(id=user.pk)
                login(request,usu)
                try:
                    nome = f'{usu.first_name} {usu.last_name}'
                    inicial = f'{usu.first_name[0]}{usu.last_name[0]}'
                except:
                    pass
                ret = f'status:ok,avatar:{usu.avatar.menu},userid:{nome},inicial:{inicial},sessionid:{usu.get_session_auth_hash()}'
                return HttpResponse(ret)
            else:
                return HttpResponse('usuario')
        except Exception as ex:
            return HttpResponse(f'falha - {str(ex)}')
            
@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self,request):
        if request.user.is_authenticated:
            u = request.user
            print(u)
            user = Usuario.objects.get(email=u)
            return HttpResponse(f'{user.first_name},{user.last_name},{user.groups.first()},{user.avatar}')
        else:
            return HttpResponse('falha - sem premissão!')