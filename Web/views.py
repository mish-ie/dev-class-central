from django.shortcuts import render, get_object_or_404
from googletrans import Translator

def my_view(request):
    text = "Find| your next course."
    
    
def home(request):
    text = "Find| your next course."
    lang = 'hi'
    translator = Translator()
    translated_text = translator.translate(text, dest=lang).text
    translated_text = re.sub(r'\|', ' ', translated_text)
    
    return render(request, 'Home/Home.html', {'translated_text': translated_text})