from django.urls import path

from todo.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TagsListView,
    TodoDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    complete_or_undo,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),
    path("tags", TagsListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("complete_or_undo/<int:pk>/", complete_or_undo, name="task_complete_undo"),
]

app_name = "todo"
