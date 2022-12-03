from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Todo
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


class TodoListview(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'task'

class TodoDetailview(DetailView):
    model = Todo
    template_name = 'details.html'
    context_object_name = 'task'

class TodoUpdateview(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})

class TodoDeleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


# Create your views here.
def add(request):
    task = Todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        Task=Todo(name=name,priority=priority,date=date)
        Task.save()
    return render(request,'home.html',{'task':task})

#def details(request):

  #  return render(request,'details.html',{'task':task})
def delete(request,taskid):
    task=Todo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request, taskid):
    task=Todo.objects.get(id=taskid)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form':form, 'task':task})