"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include,path
from medi import views

urlpatterns = [
    

    path('admin/', admin.site.urls),
    path('', views.index),
    path('frame2.html', views.f2,name='frame2.html'),
    path('frame3.html', views.f3,name='frame3.html'),
    path('frame4.html', views.f4,name='frame4.html'),
    path('frame5.html', views.f5,name='frame5.html'),
    path('frame6.html', views.f6,name='frame6.html'),
    path('frame7.html', views.f7,name='frame7.html'),
    path('frame8.html', views.f8,name='frame8.html'),
    path('frame10.html', views.f10,name='frame10.html'),
    path('frame11.html', views.f11,name='frame11.html'),
    path('last-frame.html',views.flast,name='last-frame.html')
    
    
    
    
]
