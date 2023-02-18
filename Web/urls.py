from django.urls import path
from . import views

app_name = 'Web'

urlpatterns = [
    path('', views.home, name='home'),
    path('help/moocs/', views.help, name='help'),)
    
    path('courses/', views.Courses, name='Courses'),
    path('course/', views.Course, name='Course'),
    path('instituitions/', views.Institutions, name='Institutions'),
    path('instituition/', views.Institution, name='Institution'),
    path('rankings/', views.Rankings, name='Rankings'),
    path('ranking/', views.Ranking, name='Ranking'),   
    
    path('collections/', views.Collections, name='Collections'),
    path('collection/', views.Collection, name='Collection'),
    
    path('subject/', views.Subject, name='Subject'),
    path('uni/', views.Uni, name='Uni'),
    path('providers/', views.Providers, name='Providers'),
    path('provider/', views.Provider, name='Provider'), 
    path('reports/', views.Reports, name='Reports'),
    path('report/', views.Report, name='Report'),



    # Defined New Strategy
    path('report/free-certificates/', views.free_certificates, name='FreeCertificates'),
    path('report/category/best-courses/', views.rbest_courses, name='rbest_courses'),
    path('report/online-learning-deals/', views.online_learning_deals, name='ronline_learning'),
    
    
    
    path('subjects/', views.Subjects, name='Subjects'),
    path('subject/cs/', views.computer_science, name='cs'),
    path('subject/business/', views.business, name='business'),




    path('universities/', views.University, name='University'),
    path('university/stanford/', views.stanford, name='stanford'),
    path('university/mit/', views.mit, name='mit'),
    
    path('collection/top-free-online-courses/', views.best_off_all_time, name='best_off_all_time'),
    path('collection/sustainability-online-courses/', views.sustainability, name='sustainability'),
    path('collection/ivy-league-moocs/', views.ivy_league, name='ivy_league'),
    
    
    path('institution/google/', views.google, name='google'),
    path('institution/amazon/', views.amazon, name='amazon'),

    
]
