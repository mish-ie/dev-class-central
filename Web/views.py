from django.shortcuts import render, get_object_or_404
from googletrans import Translator
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext


    
def home(request):
    trans=translate(language='hi')
    return render(request, 'Home/Home.html',{'trans':trans})
 
 def Courses(request):
    return render(request, 'Courses')
 
 def Course(request):
    return render(request, 'Courses')
 
 
 
 def Institutions(request):
    return render(request, 'Institutions')
 
 def Institution(request):
    return render(request, 'Institutions')
 
 
 
 def Rankings(request):
    return render(request, 'Rankings')
 
 def Ranking(request):
    return render(request, 'Rankings')
 
 
 
 def Collections(request):
    return render(request, 'Collections')
 
 def Collection(request):
    return render(request, 'Collections')
 
 
 
 def Subjects(request):
    return render(request, 'Subjects')
 
  def Subject(request):
    return render(request, 'Subjects')
 
 
 
 def University(request):
    return render(request, 'University')
 
  def Uni(request):
    return render(request, 'University')
 
 
 
 def Providers(request):
    return render(request, 'Providers')
 
  def Provider(request):
    return render(request, 'Providers')
 
 
 
 def Reports(request):
    return render(request, 'Reports')
 
  def Report(request):
    return render(request, 'Reports')
 
 
 