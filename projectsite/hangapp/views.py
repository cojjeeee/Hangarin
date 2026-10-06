from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hangapp.models import Task, SubTask, Note
from hangapp.forms import TaskForm, SubTaskForm, NoteForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

# Create your views here.

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.count()
        context["total_subtasks"] = SubTask.objects.count()
        return context

########################### TASK ###########################
########################### TASK ###########################
########################### TASK ###########################

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["title", "deadline", "status", "category__name", "priority__name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(deadline=query)
            )
        return qs

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

########################### SUBTASK ###########################
########################### SUBTASK ###########################
########################### SUBTASK ###########################

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'stask'
    template_name = 'stask_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["parent_task", "title", "status"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(parent_task__icontains=query) |
                Q(title__icontains=query)
            )
        return qs

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'stask_form.html'
    success_url = reverse_lazy('stask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'stask_form.html'
    success_url = reverse_lazy('stask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'stask_del.html'
    success_url = reverse_lazy('stask-list')

########################### NOTES ###########################
########################### NOTES ###########################
########################### NOTES ###########################

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["task__title", "content"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "task__title"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(task__title__icontains=query) |
                Q(content__icontains=query)
            )
        return qs

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')