import datetime

from django import forms
from django.forms import DateTimeInput

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        initial=datetime.datetime.today,
        required=False,
        widget=DateTimeInput(attrs={"type": "datetime-local"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tags"]
