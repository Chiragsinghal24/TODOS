from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.alltodos,name ='alltodos'),
    path('',views.Signuppage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('delete_item/<int:pk>',views.deleteItem,name = 'deleteItem'),
    path('update_item<int:pk>',views.updateItem,name = 'updateItem'),
    path('logout/',views.Logoutpage,name='logout'),
]