# is we define routes!
from django.urls import path

from .views import HomePageView


# urlpatterns <-- named specifically for django
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
