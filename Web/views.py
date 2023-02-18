from django.shortcuts import render, get_object_or_404
from googletrans import Translator
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext


    
def home(request):
   #  trans=translate(language='hi')
   return render(request, 'Home/Home.html')
 
def free_certificates(request):
   return render(request, 'Courses/free-cert.html')











def Courses(request):
   return render(request, 'Courses/Courses.html')
 
def Course(request):
   return render(request, 'Courses/Course.html')

 
def Institutions(request):
   return render(request, 'Institutions/Institutions.html')
 
def Institution(request):
   return render(request, 'Institutions/Institution.html')
 
 
 
def Rankings(request):
   return render(request, 'Rankings/Rankings.html')
 
def Ranking(request):
   return render(request, 'Rankings/Ranking.html')
 
 
 
def Collections(request):
   return render(request, 'Collections/Collections.html')
 
def Collection(request):
   return render(request, 'Collections/Collection.html')
  
def Subjects(request):
   return render(request, 'Subjects/Subjects.html')

def Subject(request):
   return render(request, 'Subjects/Subject.html')
 
  
def University(request):
   return render(request, 'University/University.html')
 
def Uni(request):
   return render(request, 'University/Uni.html')
 
 
 
def Providers(request):
   return render(request, 'Providers/Providers.html')
 
def Provider(request):
   return render(request, 'Providers/Provider.html')
 
 
 
def Reports(request):
   return render(request, 'Reports/Reports.html')
 
def Report(request):
   return render(request, 'Reports/Report.html')
 
 
 