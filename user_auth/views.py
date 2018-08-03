from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



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



class LoginView(View):

    def get(self, request):
        template = loader.get_template('user_auth/login.html')
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request):
        print(request.POST)
        data = {}
        data['password'] = request.POST.get('password')
        data['username'] = request.POST.get('username')
        print(data)

        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_worker:
                    return HttpResponseRedirect('/worker/')
                else:
                    return HttpResponseRedirect('/consumer/')
        else:
            template = loader.get_template('user_auth/login.html')
            context = {'error': 'Invalid credentials'}
            return HttpResponse(template.render(context, request))


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/users/login/')

    # Redirect to a success page.




def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
