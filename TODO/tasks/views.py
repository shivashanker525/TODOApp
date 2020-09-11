from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from rest_framework import viewsets
from .serializers import TaskSerializer
# Create your views here.

def taskpage(request):
    tasks = Task.objects.all()
    form = TaskForm
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasklist.html',context)

def updatetask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'updatetask.html',context)

def deletetask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'deletetask.html',context)

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]