from django import template
from googletrans import Translator

register = template.Library()

@register.filter
def translate(value, lang):
    translator = Translator()
    return translator.translate(value, dest=lang).text