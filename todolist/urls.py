from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('createtask/', create_task, name='create_task')
]