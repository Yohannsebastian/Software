from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name="inicio"),
    path('salary', views.salarios, name= 'salary'),
    path("save/", views.save, name="save"),
    path('job/', views.job, name="job"),
    path('savejob', views.savejob, name="savejob")
]


