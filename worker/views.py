from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.db.models import Q

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
from django.utils.decorators import method_decorator
from django.views import View

from consumer.models import ConsumerTask

from django.http import HttpResponse
from user_auth.helpers import worker_required



def index(request):
    print(request)
    template = loader.get_template('worker/home.html')
    context = {}
    return HttpResponse(template.render(context, request))


@method_decorator([login_required, worker_required], name='dispatch')
class TaskList(View):

    def get(self, request):
        template = loader.get_template('worker/task_list.html')
        context = {}
        tasks = ConsumerTask.objects.filter(Q(status=ConsumerTask.CREATED))
        if tasks:
            context['tasks'] = tasks
        return HttpResponse(template.render(context, request))

@method_decorator([login_required, worker_required], name='dispatch')
class TaskAccept(View):
    def get(self, request, task_id):
        task = ConsumerTask.objects.filter(Q(id=task_id) & ~Q(status=ConsumerTask.COMPLETED)).first()
        task.worker = request.user
        task.status = ConsumerTask.IN_PROGRESS
        task.save()
        return redirect('/worker/task-list')

@method_decorator([login_required, worker_required], name='dispatch')
class MyTaskList(View):
    def get(self, request):
        template = loader.get_template('worker/task_list.html')
        context = {}
        tasks = ConsumerTask.objects.filter(user=request.user)
        if tasks:
            context['tasks'] = tasks
        return HttpResponse(template.render(context, request))
