from pages import views
from django.urls import path

app_name = "pages"
urlpatterns = [
    path('', views.indexpage_view, name='index'),
    path('homepage/', views.homepage_view, name='home'),
    path('about/', views.aboutpage_view, name='about'),
    path('services/', views.servicespage_view, name='services'),
]
