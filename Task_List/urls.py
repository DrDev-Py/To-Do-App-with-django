from django.urls import path
from .views import(
TaskCreateView, TaskListView, TaskDeleteView, TaskDetailView
)

app_name = 'task'
urlpatterns = [
    path('home/', TaskCreateView, name='home'),
    path('list/', TaskListView.as_view(), name='list'),
    path('delete/<int:id>/', TaskDeleteView, name='delete'),
    path('detail/<int:id>/', TaskDetailView, name='detail'),
]
