from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.
def todo(request):
    todo_items = Todo.objects.all().order_by("-date")
    return render(request,'todo.html',{'todo_items': todo_items})

@csrf_exempt
def add(request):
    current_date = timezone.now()
    content = request.POST['text']
    Todo.objects.create(date=current_date,text=content)

    # return render(request,'todo.html',{'adds': add1})
        
    return HttpResponseRedirect('/')

@csrf_exempt
def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

@csrf_exempt
def deleteAll(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect('/')