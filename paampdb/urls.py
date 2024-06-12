"""
URL configuration for paampdb project.

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
from django.urls import path
from docking import views

app_name = "paampdb"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexPage,name='index'),
    path('enter/',views.EnterPage,name='enter'),
    path("home/", views.search_view, name="home"),
    path('protein/<int:proteins_id>/', views.protein, name='protein'),
    path('search/', views.search_view, name='search'),   
    path('create_protien/', views.create_protein, name='create_protein'),
    #path('amp/<int:amp_id>/target/<int:target_protein_id>/', views.dock_complexes, name='dock_complexes'),
    #path('target_proteins/', views.target_proteins, name='target_proteins'),
    path("stats/", views.StatsPage, name="stats"),
    path("about/", views.AboutUsPage, name="about_us"),
    path("tutorial/", views.TutorialPage, name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),

]
