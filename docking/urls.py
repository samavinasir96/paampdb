from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from .import views

app_name = "abampdb"
urlpatterns = [
    path('',views.IndexPage,name='index'),
    path('enter/',views.EnterPage,name='enter'),
    path("home/", views.search_view, name="home"),
    path("<int:proteins_id>", views.protein, name='protein'),
    path('search/', views.search_view, name='search'),   
    path('create_protien/', views.create_protien, name='create_protein'),
    path('<int:proteins_id>/target_proteins', views.target_proteins, name='target_proteins'),
    path('serve-pdb/<int:dock_id>/', views.serve_amp_pdb, name='serve_pdb'),
    path("stats/", views.StatsPage, name="stats"),
    path("about/", views.AboutUsPage, name="about_us"),
    path("tutorial/", views.TutorialPage, name="tutorial"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path("docking/", views.get_search_results, name="docking"),