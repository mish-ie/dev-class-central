from django.shortcuts import render, get_object_or_404
from googletrans import Translator
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext


    
def home(request):
   #  trans=translate(language='hi')
   return render(request, 'Home/Home.html')

def help(request):
   return render(request, 'Home/Help.html')

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
def ivy_league(request):
   return render(request, 'Collections/ivy_league.html')

def sustainability(request):
   return render(request, 'Collections/sustainability.html')

def best_off_all_time(request):
   return render(request, 'Collections/best_off_all_time.html')


# Universities
def University(request):
   return render(request, 'University/University.html')

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
   return render(request, 'Institutions/Institutions.html')

def google(request):
   return render(request, 'Instituitions/google.html')

def amazon(request):
   return render(request, 'Instituitions/amazon.html')






# Subject:
def Subjects(request):
   return render(request, 'Subjects/Subjects.html')
 


# Providers
def Providers(request):
   return render(request, 'Providers/Providers.html')
 
def coursera(request):
   return render(request, 'Providers/coursera.html')

def Edx(request):
   return render(request, 'Providers/Edx.html')

def futurelearn(request):
   return render(request, 'Providers/futurelearn.html')

def udemy(request):
   return render(request, 'Providers/udemy.html')

def linkedin_learning(request):
   return render(request, 'Providers/linkedin_learning.html')

def skillshare(request):
   return render(request, 'Providers/skillshare.html')



# Ranking
def Rankings(request):
   return render(request, 'Rankings/Rankings.html')









def Courses(request):
   return render(request, 'Courses/Courses.html')
 
def Course(request):
   return render(request, 'Courses/Course.html') 
def Institution(request):
   return render(request, 'Institutions/Institution.html') 
def Ranking(request):
   return render(request, 'Rankings/Ranking.html')
 
 
 
def Collections(request):
   return render(request, 'Collections/Collections.html')
 
def Collection(request):
   return render(request, 'Collections/Collection.html')
def Subject(request):
   return render(request, 'Subjects/Subject.html')
def Uni(request):
   return render(request, 'University/Uni.html')
def Provider(request):
   return render(request, 'Providers/Provider.html')
 
 
 
def Reports(request):
   return render(request, 'Reports/Reports.html')
 
def Report(request):
   return render(request, 'Reports/Report.html')
 
 
 