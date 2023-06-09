from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("pages/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
