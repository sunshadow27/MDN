"""MDN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('demo/', views.demo),
    path('login/', views.login),
    path('register/', views.register),
    path('manager_menu/',views.manager_menu),
    path('manager_add_user/',views.manager_add_user),
    path('manager_edit_user/',views.manager_edit_user),
    path('manager_del_user/',views.manager_del_user),
    path('show_article/',views.show_article),
    path('write/',views.write),
    path('modal_add_user/',views.modal_add_user),
    path('modal_edit_user/',views.modal_edit_user),
    path('mother_modal/',views.mother_modal),
]
