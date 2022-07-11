from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class TodoListView(generic.ListView):
    queryset = Task.objects.order_by("done", "-datetime")
    model = Task


class TodoCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:todo_list")
    form_class = TaskForm


class TodoUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:todo_list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/todo-delete.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:todo_list")


class TagsListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_delete.html"
    success_url = reverse_lazy("todo:tags_list")


def complete_or_undo(request, pk):
    task = Task.objects.get(id=pk)
    if not task.done:
        task.done = True
    else:
        task.done = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:todo_list"))
