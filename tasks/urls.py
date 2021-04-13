"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views, user_auth_views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete_task'),
    path('complete/<int:id>/', views.complete, name='completed_task'),
    path('', views.tasks, name='tasks'),
    path('signin', user_auth_views.sign_in, name='sign_in_user'),
    path('signup', user_auth_views.signup, name='signup_form')
]