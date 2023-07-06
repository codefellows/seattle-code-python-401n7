from django.urls import path
from .views import ThingList, ThingDetail

# ThingList will list all of the things in our Thing table
# ThingDetail will show all of the fields for one of the things

urlpatterns = [
    path('', ThingList.as_view()),  # don't need the `name='thing_list'`
    path('<int:pk>/', ThingDetail.as_view()),
]
