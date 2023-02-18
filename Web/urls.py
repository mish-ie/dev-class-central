from django.urls import path
from . import views

app_name = 'Web'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('courses/', views.Courses, name='Courses'),
    path('course/', views.Course, name='Course'),
    
    path('instituitions/', views.Institutions, name='Institutions'),
    path('instituition/', views.Institution, name='Institution'),
    
    path('rankings/', views.Rankings, name='Rankings'),
    path('ranking/', views.Ranking, name='Ranking'),   
    
    path('collections/', views.Collections, name='Collections'),
    path('collection/', views.Collection, name='Collection'),
    
    path('subjects/', views.Subjects, name='Subjects'),
    path('subject/', views.Subject, name='Subject'),
    
    path('university/', views.University, name='University'),
    path('uni/', views.Uni, name='Uni'),
    
    path('providers/', views.Providers, name='Providers'),
    path('provider/', views.Provider, name='Provider'), 
    
    path('reports/', views.Reports, name='Reports'),
    path('report/', views.Report, name='Report'),
]
