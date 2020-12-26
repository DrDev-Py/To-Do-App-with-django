from django.shortcuts import (
render,
get_object_or_404,
redirect
)
from django.urls import reverse

from .models import Task
from .forms import TaskForm

from django.views.generic import(
    CreateView,
    ListView
)
# Create your views here.


"""class TaskCreateView(CreateView):
    template_name = 'Task_List/task_create.html'
    form_class = TaskForm
    success_url = '/#'"""


def TaskCreateView(request):
    """def get_absolute_url(self):
        return reverse("task: list")"""
    form = TaskForm() #request.POST or None
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)
            form = TaskForm()
            return redirect('/task/list/')

    context = {'form': form}
    return render(request, "Task_List/task_create.html", context)



class TaskListView(ListView):
    template_name = 'Task_List/task_list.html'
    queryset = Task.objects.all()
    #number = queryset.count()


def TaskDeleteView(request, id):
    obj = get_object_or_404(Task, id=id )
    if request.method == 'POST':
        obj.delete()
        return redirect('/task/list')

    context={'object': obj}
    return render(request, "Task_List/task_delete.html", context)



def TaskDetailView(request, id):
    obj = get_object_or_404(Task, id=id)
    context={'object': obj}
    return render(request, "Task_List/task_detail.html", context)
