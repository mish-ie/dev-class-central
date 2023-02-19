from django.urls import path
from . import views

app_name = 'Web'

urlpatterns = [
    path('', views.home, name='home'),
    path('help/moocs/', views.help, name='help'),
    
    path('courses/', views.Courses, name='Courses'),
    path('course/', views.Course, name='Course'),
    path('instituition/', views.Institution, name='Institution'),
    path('ranking/', views.Ranking, name='Ranking'),   
    
    path('collections/', views.Collections, name='Collections'),
    path('collection/', views.Collection, name='Collection'),
    
    path('subject/', views.Subject, name='Subject'),
    path('uni/', views.Uni, name='Uni'),
    path('provider/', views.Provider, name='Provider'), 
    path('reports/', views.Reports, name='Reports'),
    path('report/', views.Report, name='Report'),



    # Defined New Strategy
    path('report/free-certificates/', views.free_certificates, name='FreeCertificates'),
    path('report/category/best-courses/', views.rbest_courses, name='rbest_courses'),
    path('report/online-learning-deals/', views.online_learning_deals, name='ronline_learning'),
    path('report/udemy-layoffs/', views.udemy_layoffs, name='udemy_layoffs'),
    path('report/harvard-cs50-guide/', views.harvard_cs50_guide, name='harvard_cs'),
    path('report/chinese-mooc-platforms/', views.chinese_mooc_platforms, name='chinese_mooc_platforms'),
    path('report/futurelearn-expands-paywall/', views.futurelearn_expands_paywall, name='futurelearn_expands'),
    path('report/udemy-by-the-numbers/', views.udemy_by_the_numbers, name='udemy_by_the_numbers'),
    path('report/domestika-layoffs/', views.domestika_layoffs, name='domestika_lay'),
    path('report/thinkific-layoffs/', views.thinkific_layoffs, name='thinkific_lay'),
    path('report/udemy-new-ceo/', views.udemy_new_ceo, name='udemy_new_ceo'),
    path('report/cs50-free-certificate/', views.cs50_free_certificate, name='cs50_free_certificate'),
    path('report/best-davinci-resolve-courses/', views.best_davinci_resolve_courses, name='best_davinci_resolve_courses'),
    path('report/best-free-prolog-courses/', views.best_free_prolog_courses, name='best_free_prolog_courses'),
    path('report/best-japanese-courses/', views.best_japanese_courses, name='best_japanese_courses'),
    path('report/best-erlang-courses/', views.best_erlang_courses, name='best_erlang_courses'),
    path('report/best-css-animation-courses/', views.best_css_animation_courses, name='best_css_animation_courses'),
    
    
    
    
    path('rankings/', views.Rankings, name='Rankings'),

    
    path('subjects/', views.Subjects, name='Subjects'),
    path('subject/cs/', views.computer_science, name='cs'),
    path('subject/business/', views.business, name='business'),
    
    
    path('providers/', views.Providers, name='Providers'),
    path('provider/coursera/', views.coursera, name='coursera'),
    path('provider/edx/', views.Edx, name='Edx'),
    path('provider/futurelearn/', views.futurelearn, name='futurelearn'),
    path('provider/udemy/', views.udemy, name='udemy'),
    path('provider/swayam/', views.swayam, name='swayam'),
    path('provider/linkedin-learning/', views.linkedin_learning, name='linkedin_learning'),
    path('provider/skillshare/', views.skillshare, name='skillshare'),




    path('universities/', views.University, name='University'),
    path('university/stanford/', views.stanford, name='stanford'),
    path('university/mit/', views.mit, name='mit'),
    path('university/harvard/', views.harvard, name='harvard'),
    path('university/iit-kharagpur/', views.iit_kharagpur, name='iit_kharagpur'),
    path('university/rice/', views.rice, name='rice'),
    path('university/columbia/', views.columbia, name='columbia'),
    path('university/edinburgh/', views.edinburgh, name='edinburgh'),
    path('university/penn/', views.penn, name='penn'),
    path('university/umich/', views.umich, name='umich'),
    path('university/iitm/', views.iitm, name='iitm'),
    path('university/cornell/', views.cornell, name='cornell'),
    path('university/purdue/',views.purdue, name='purdue'),
    path('university/duke/', views.duke, name='duke'),
    
    
    
    path('collection/top-free-online-courses/', views.best_off_all_time, name='best_off_all_time'),
    path('collection/sustainability-online-courses/', views.sustainability, name='sustainability'),
    path('collection/ivy-league-moocs/', views.ivy_league, name='ivy_league'),
    
    
    path('institutions/', views.Institutions, name='Institutions'),
    path('institution/google/', views.google, name='google'),
    path('institution/amazon/', views.amazon, name='amazon'),
    path('institution/microsoft/', views.microsoft, name='microsoft'),
    path('institution/ibm/', views.ibm, name='ibm'),
    path('institution/smithsonian/', views.smithsonian, name='smithsonian'),
    path('provider/unccelearn/', views.unccelearn, name='unccelearn'),
    path('nstitution/british-council/', views.british_council, name='british_council'),

    
]
