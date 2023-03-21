"""TRCC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, re_path
from empirer import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),    
    path('program/', views.program, name='program'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),

    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    
    path("programs-list/", views.programsList, name="programs_list"),
    path("decision/", views.decision, name="decision"),
    path('new/weekly-program/', views.createWeekly, name="create_weekly"),
    path("update/weekly-program/<int:pk>/", views.updateWeekly, name="update_weekly"),
    path("delete/weekly-program/<int:pk>/", views.deleteWeekly, name="delete_weekly"),

    path('new/live-program/', views.createLive, name="create_live"),
    path("update/live-program/<int:pk>/", views.updateLive, name="update_live"),
    path("delete/live-program/<int:pk>/", views.deleteLive, name="delete_live"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('.well-known/pki-validation/52B0311E4A32747D48B4673CFBB46465.txt', views.read_file, name='read_file'),
]
