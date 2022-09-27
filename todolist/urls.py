from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, update_data, delete_data

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('', update_data, name='update_data'),
    path('', delete_data, name='delete_data')
]