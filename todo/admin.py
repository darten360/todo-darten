from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ("content", "deadline", "done")
    list_filter = ("done", "datetime")
    search_fields = ("tags", "content")
