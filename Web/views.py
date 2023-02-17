from django.shortcuts import render, get_object_or_404
from googletrans import Translator
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext



def translate(language):
   cur_language=get_language()
   try:
      activate(language)
      text=gettext('how are you')
   finally:
       activate(cur_language)
   return text 
    
def home(request):
    trans=translate(language='hi')
  
    return render(request, 'Home/Home.html',{'trans':trans})