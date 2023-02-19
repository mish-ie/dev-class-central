from django.urls import path
from . import views

app_name = 'Web'

urlpatterns = [
    path('', views.home, name='home'),
    path('help/moocs/', views.get_help, name='help'),
    path('about/', views.about, name='about'),
    path('help/', views.faqs, name='faqs'),
    path('about/privacy-policy/', views.privacy_policy, name='privacy'),
    path('about/careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
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
    path('report/udemy-top-courses/', views.udemy_top_courses, name='udemy_top_courses'),
    path('report/india-online-degrees/', views.india_online_degrees, name='india_online_degrees'),
    path('report/mooc-based-masters-degree/', views.mooc_based_masters_degree, name='mooc_based_masters_degree'),
    path('report/most-popular-online-courses/', views.most_popular_online_courses, name='most_popular_online_courses'),
    path('report/list-of-mooc-based-microcredentials/', views.most_popular_online_courses, name='most_popular_online_courses'),
    path('report/best-free-online-courses-2022/', views.best_free_online_courses_2022, name='best_free_online_courses_2022'),
    path('report/most-popular-courses-2023/', views.best_free_online_courses_2023, name='best_free_online_courses_2023'),
    path('report/coursera-top-courses/', views.coursera_top_courses_2023, name='coursera_top_courses_2023'),
    path('report/edx-top-courses/', views.edx_top_courses, name='edx_top_courses'),
    path('report/2022-year-in-review/', views.the_2022_year_in_review, name='2022_year_in_review'),
    path('report/class-central-ddos-attack/', views.central_ddos_attack, name='ddos_attack'),
    path('report/open-university-insiders-perspective/', views.open_university_insiders_perspective, name='open_university_insiders_perspective'),
    path('report/free-google-certifications/', views.free_google_certifications, name='free_google_cert'),
    path('report/linkedin-learning-free-learning-paths/', views.linkedin_learning_free_learning_paths, name='flinkedin_learning'),
    path('report/coursera-free-online-courses/', views.coursera_free_online_courses, name='fcoursera'),
    path('report/writing-free-online-courses/', views.writing_free_online_courses, name='writing_free'),
    path('report/review-exploratory-data-analysis-matlab/', views.data_analysis_matlab, name='data_analysis_matlab'),
    path('report/review-learning-to-teach/', views.learn_to_teach, name='learn_to_teach'),
    path('report/most-popular-march-2023/', views.most_popular_march_2023, name='most_popular_march_2023'),
    
    
    path('report/author/dhawal/', views.author_dhawal, name='author_dhawal'),
    
    path('rankings/', views.Rankings, name='Rankings'),

    
    path('subjects/', views.Subjects, name='Subjects'),
    path('subject/cs/', views.computer_science, name='cs'),
    path('subject/business/', views.business, name='business'),
    path('subject/psychology/', views.Psychology, name='Psychology'),
    path('subject/cybersecurity/', views.cybersecurity, name='cybersecurity'),
    path('subject/law/', views.law, name='law'),
    path('subject/health/', views.health, name='health'),
    path('subject/accounting/', views.accounting, name='accounting'),
    path('subject/web-development/', views.web_development, name='web_development'),
    
    
    path('providers/', views.Providers, name='Providers'),
    path('provider/coursera/', views.coursera, name='coursera'),
    path('provider/edx/', views.Edx, name='Edx'),
    path('provider/futurelearn/', views.futurelearn, name='futurelearn'),
    path('provider/udemy/', views.udemy, name='udemy'),
    path('provider/swayam/', views.swayam, name='swayam'),
    path('provider/linkedin-learning/', views.linkedin_learning, name='linkedin_learning'),
    path('provider/skillshare/', views.skillshare, name='skillshare'),
    path('provider/udacity/', views.udacity, name='udacity'),
    path('provider/unccelearn/', views.unccelearn, name='unccelearn'),





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
    path('university/gatech/', views.gatech, name='gatech'),
    
    
    
    path('collection/top-free-online-courses/', views.best_off_all_time, name='best_off_all_time'),
    path('collection/sustainability-online-courses/', views.sustainability, name='sustainability'),
    path('collection/ivy-league-moocs/', views.ivy_league, name='ivy_league'),
    
    
    path('institutions/', views.Institutions, name='Institutions'),
    path('institution/google/', views.google, name='google'),
    path('institution/amazon/', views.amazon, name='amazon'),
    path('institution/microsoft/', views.microsoft, name='microsoft'),
    path('institution/ibm/', views.ibm, name='ibm'),
    path('institution/smithsonian/', views.smithsonian, name='smithsonian'),
    path('institution/british-council/', views.british_council, name='british_council'),
    path('institution/salesforce/', views.salesforce, name='salesforce'),
    path('institution/linuxfoundation/', views.linuxfoundation, name='linuxfoundation'),

    
]
