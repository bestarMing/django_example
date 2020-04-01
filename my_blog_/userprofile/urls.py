from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),

]