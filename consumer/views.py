from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

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
from django.views import View

from consumer.models import ConsumerTask
from .helpers import create_task



def index(request):
    return HttpResponse("Hello, world. You're at the consumer index.")




class CreateTask(View):

    def get(self, request):
        print(request)
        template = loader.get_template('consumer/task_create.html')
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request):
        print(request.POST)
        data = {}
        data['name'] = request.POST.get('name')
        data['category'] = request.POST.get('category')
        data['description'] = request.POST.get('description')
        print(data)
        task = create_task(request=request, data= data)
        print(task.__dict__)
        return redirect('/consumer/task-list')

class TaskList(View):
    def get(self, request):
        template = loader.get_template('consumer/task_list.html')
        context = {}
        tasks = ConsumerTask.objects.filter(user=request.user)
        context['tasks'] = tasks
        return HttpResponse(template.render(context, request))

