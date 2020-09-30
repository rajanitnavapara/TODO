from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add',views.add, name='add'),
    path('',views.todo,name='todo'),
    path('todo',views.todo,name='todo'),
    path('delete/<int:todo_id>',views.delete),
    path('deleteall',views.deleteAll),
]   