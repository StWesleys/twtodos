# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Todo

# def todo_list(resquest):
#     # modelo + .objects.all() usado para pegar todo o conteúdo do db 
#     todos = Todo.objects.all()
#     return render(resquest, "todos/todo_list.html", { "todos": todos })

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model  = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")