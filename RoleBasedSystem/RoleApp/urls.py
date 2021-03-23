from django.urls import path
from RoleApp import views
from .views import Index
from .views import Dashboard
from .views import CreateUser
from .views import AdminLogin
from .views import UserList
from .views import permission
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="Home"),
    path('dashboard', auth_middleware(Dashboard.as_view()), name="Dashboard"),
    path('CreateUser', CreateUser.as_view(), name="CreateUser"),
    path('AdminLogin', AdminLogin.as_view(), name="AdminLogin"),
    path('UserList', UserList.as_view(), name="UserList"),
    path('permission', permission.as_view() , name="Permission"),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.edit),  
    # path('UserCreationForm', views.CreateUser),  
    # path('load_CSC', views.load_CSC, name='ajax_load_cities')  

]
