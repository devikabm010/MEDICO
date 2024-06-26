"""
URL configuration for medicalstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from store import views

urlpatterns = [
    path('',views.store,name='home'),
    # path('',views.store,name='home'),
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('medicines/',include('medicines.urls')),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('medapi/', include('medapi.urls')),
    
]
