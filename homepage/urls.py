from django.urls import path
from . import views
from django.conf.urls import handler404
from django.conf.urls import handler500



urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("", views.homepage, name="homepage"),
    path("about", views.about, name="about"),
    path("news", views.news, name="news"),
    path("contact", views.contact, name="contact"),
]
handler404 = views.custom_404
handler500 = views.custom_500
