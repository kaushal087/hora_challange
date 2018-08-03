from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .helpers import *
# Create your views here.
from django.views import View

from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the users index.")



class SignUpView(View):

    def get(self, request):
        template = loader.get_template('user_auth/signup.html')
        context = {}
        return HttpResponse(template.render(context, request))



class WorkerSignUpView(View):

    def get(self, request):
        template = loader.get_template('user_auth/worker_signup.html')
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request):
        print(request.POST)
        data = {}
        data['name'] = request.POST.get('name')
        data['password'] = request.POST.get('password')
        data['email'] = request.POST.get('email')
        print(data)
        create_user(data, is_consumer=True)
        return redirect('/users/login/')

class ConsumerSignUpView(View):

    def get(self, request):
        template = loader.get_template('user_auth/consumer_signup.html')
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request):
        print(request.POST)
        data = {}
        data['name'] = request.POST.get('name')
        data['password'] = request.POST.get('password')
        data['email'] = request.POST.get('email')
        print(data)
        create_user(data, is_worker=True)
        return redirect('/users/login/')

