from django.urls import path 
from . import views

urlpatterns = [
    path("",views.index,name="home_pg"),
    path("<int:week>",views.weekly_in_number),
    path("<str:week>",views.weekly_challenge,name="week-challenge")
   

]
