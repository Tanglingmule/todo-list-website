# app level urls (to_do_list)
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about")
]