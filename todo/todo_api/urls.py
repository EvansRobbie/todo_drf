from django.urls import path
from . import views
# from .views import TodoApiview, TodoDetailsApiview

urlpatterns = [
    path('', views.getRoutes, name= 'routes'),
    path('todo/', views.getTodo, name='todo'),
    path('todo/<int:todo_id>/', views.getTodoDetail, name = 'todo_id'),
    path('todo/create/', views.postTodo, name= 'create'),
    path('todo/<int:todo_id>/update/', views.updateDetail, name ='update'),
    path('todo/<int:todo_id>/delete', views.deleteTodoDetail,name='delete')
    # path('todo/', TodoApiview.as_view()),
    # path('todo/<int:todo_id>/', TodoDetailsApiview.as_view())
]