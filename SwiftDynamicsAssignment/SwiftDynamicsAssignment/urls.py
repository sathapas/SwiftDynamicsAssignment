"""SwiftDynamicsAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from todoApp import views
from api.views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
    #path('', views.home),
    path('3', views.page3),
    path('4', views.page4),
    path('app3', views.app3),
    path('app4', views.app4),
    path('1', views.page1),
    path('todo_submit', views.submit, name='todo_submit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('sortdata',views.sortdata,name='sortdata'),
    path('searchdata',views.searchdata,name='searchdata'),
    path('contact',views.contact,name='contact')

    
]
