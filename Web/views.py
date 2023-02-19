from django.shortcuts import render, get_object_or_404
from googletrans import Translator
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext


    
def home(request):
   #  trans=translate(language='hi')
   return render(request, 'Home/Home.html')

def about(request):
   return render(request, 'Home/About.html')

def get_help(request):
   return render(request, 'Home/Help.html')

def faqs(request):
   return render(request, 'Home/faqs.html')

def privacy_policy(request):
   return render(request, 'Home/PrivacyPolicy.html')

def careers(request):
   return render(request, 'Home/careers.html')

def contact(request):
   return render(request, 'Home/contact.html')

# Courses
def free_certificates(request):
   return render(request, 'Courses/free-cert.html')

def rbest_courses(request):
   return render(request, 'Courses/report-best.html')

def online_learning_deals(request):
   return render(request, 'Courses/online-learning-deals.html')

def computer_science(request):
   return render(request, 'Courses/computer_science.html')

def business(request):
   return render(request, 'Courses/business.html')



# Collections

def Collections(request):
   return render(request, 'Collections/Collections.html')

def ivy_league(request):
   return render(request, 'Collections/ivy_league.html')

def sustainability(request):
   return render(request, 'Collections/sustainability.html')

def best_off_all_time(request):
   return render(request, 'Collections/best_off_all_time.html')

def udemy_top_courses(request):
   return render(request, 'Collections/udemy_top_courses.html')

def india_online_degrees(request):
   return render(request, 'Collections/india_online_degrees.html')

def mooc_based_masters_degree(request):
   return render(request, 'Collections/mooc_based_masters_degree.html')

def most_popular_online_courses(request):
   return render(request, 'Collections/most_popular_online_courses.html')


# Universities
def University(request):
   return render(request, 'University/University.html')

def gatech(request):
   return render(request, 'University/gatech.html')

def stanford(request):
   return render(request, 'University/stanford.html')

def mit(request):
   return render(request, 'University/mit.html')

def harvard(request):
   return render(request, 'University/harvard.html')

def iit_kharagpur(request):
   return render(request, 'University/iit_kharagpur.html')

def rice(request):
   return render(request, 'University/rice.html')


def columbia(request):
   return render(request, 'University/columbia.html')

def edinburgh(request):
   return render(request, 'University/edinburgh.html')

def penn(request):
   return render(request, 'University/penn.html')

def umich(request):
   return render(request, 'University/umich.html')

def iitm(request):
   return render(request, 'University/iitm.html')

def cornell(request):
   return render(request, 'University/cornell')

def purdue(request):
   return render(request, 'University/purdue.html')

def duke(request):
   return render(request, 'University/duke.html')




# Institutions
def Institutions(request):
   return render(request, 'Instituitions/Institutions.html')

def google(request):
   return render(request, 'Instituitions/google.html')

def amazon(request):
   return render(request, 'Instituitions/amazon.html')

def microsoft(request):
   return render(request, 'Instituitions/microsoft.html')

def ibm(request):
   return render(request, 'Instituitions/ibm.html')

def smithsonian(request):
   return render(request, 'Instituitions/smithsonian.html')

def unccelearn(request):
   return render(request, 'Instituitions/unccelearn.html')

def british_council(request):
   return render(request, 'Instituitions/british-council.html')

def salesforce(request):
   return render(request, 'Instituitions/salesforce.html')

def linuxfoundation(request):
   return render(request, 'Instituitions/linuxfoundation.html')



# Subject:
def Subjects(request):
   return render(request, 'Subjects/Subjects.html')

def Psychology(request):
   return render(request, 'Subjects/Psychology.html')

def cybersecurity(request):
   return render(request, 'Subjects/cybersecurity.html')

def law(request):
   return render(request, 'Subjects/law.html')

def health(request):
   return render(request, 'Subjects/health.html')

def accounting(request):
   return render(request, 'Subjects/accounting.html')

def web_development(request):
   return render(request, 'Subjects/web_development.html')
 


# Providers
def Providers(request):
   return render(request, 'Providers/Providers.html')

def udacity(request):
   return render(request, 'Providers/udacity.html')
def coursera(request):
   return render(request, 'Providers/coursera.html')

def Edx(request):
   return render(request, 'Providers/Edx.html')

def futurelearn(request):
   return render(request, 'Providers/futurelearn.html')

def udemy(request):
   return render(request, 'Providers/udemy.html')

def swayam(request):
   return render(request, 'Providers/swayam.html')

def linkedin_learning(request):
   return render(request, 'Providers/linkedin_learning.html')

def skillshare(request):
   return render(request, 'Providers/skillshare.html')



# Ranking
def Rankings(request):
   return render(request, 'Rankings/Rankings.html')


# Reports:
def Reports(request):
   return render(request, 'Reports/Reports.html')

def the_2022_year_in_review(request):
   return render(request, 'Reports/the_2022_year_in_review.html')

def central_ddos_attack(request):
   return render(request, 'Reports/central_ddos_attack.html')

def open_university_insiders_perspective(request):
   return render(request, 'Reports/open_university_insiders_perspective.html')

def free_google_certifications(request):
   return render(request, 'Reports/free_google_certifications.html')

def linkedin_learning_free_learning_paths(request):
   return render(request, 'Reports/linkedin_learning_free_learning.html')

def coursera_free_online_courses(request):
   return render(request, 'Reports/coursera_free_online_courses.html')

def writing_free_online_courses(request):
   return render(request, 'Reports/writing_free_online_courses.html')

def best_free_online_courses_2022(request):
   return render(request, 'Reports/best_free_online_courses_2022.html')

def best_free_online_courses_2023(request):
   return render(request, 'Reports/best_free_online_courses_2023.html')

def coursera_top_courses_2023(request):
   return render(request, 'Reports/coursera_top_courses_2023.html')

def edx_top_courses(request):
   return render(request, 'Reports/edx_top_courses.html')

def udemy_layoffs(request):
   return render(request, 'Reports/udemy_layoffs.html')

def harvard_cs50_guide(request):
   return render(request, 'Reports/harvard_cs50_guide.html')

def chinese_mooc_platforms(request):
   return render(request, 'Reports/chinese_mooc_platforms.html')

def futurelearn_expands_paywall(request):
   return render(request, 'Reports/futurelearn_expands_paywall.html')

def udemy_by_the_numbers(request):
   return render(request, 'Reports/udemy_by_the_numbers.html')

def domestika_layoffs(request):
   return render(request, 'Reports/domestika_layoffs.html')

def thinkific_layoffs(request):
   return render(request, 'Reports/thinkific_layoffs.html')

def udemy_new_ceo(request):
   return render(request, 'Reports/udemy_new_ceo.html')

def cs50_free_certificate(request):
   return render(request, 'Reports/cs50_free_certificate.html')

def best_davinci_resolve_courses(request):
   return render(request, 'Reports/best_davinci_resolve_courses.html')

def best_free_prolog_courses(request):
   return render(request, 'Reports/best_free_prolog_courses.html')

def best_japanese_courses(request):
   return render(request, 'Reports/best_japanese_courses.html')

def best_erlang_courses(request):
   return render(request, 'Reports/best_erlang_courses.html')

def best_css_animation_courses(request):
   return render(request, 'Reports/best_css_animation_courses.html')



def Courses(request):
   return render(request, 'Courses/Courses.html')


 
 
def Course(request):
   return render(request, 'Courses/Course.html') 
def Institution(request):
   return render(request, 'Institutions/Institution.html') 
def Ranking(request):
   return render(request, 'Rankings/Ranking.html')
def Collection(request):
   return render(request, 'Collections/Collection.html')
def Subject(request):
   return render(request, 'Subjects/Subject.html')
def Uni(request):
   return render(request, 'University/Uni.html')
def Provider(request):
   return render(request, 'Providers/Provider.html')
def Report(request):
   return render(request, 'Reports/Report.html')
 
 
 