from django.shortcuts import render
from languages.models import Language
import translators as ts


def indexpage_view(request):
    return render(request, "pages/index.html", {})

def homepage_view(request):
    if request.method == "POST":
        
        if 'selectform' in request.POST:
            request.session['language'] = request.POST.get('language')
        

        message = request.POST.get('send') or " "
        translate_to = request.session.get("language") or "fr"
        
        translator_engine:str ="google"
        translate_from = "auto"

        translated = ts.translate_text(query_text=message, translator=translator_engine, str=translate_from, to_language=translate_to)

        context = {
            "message":message,
            "message_lang":translate_from,
            "translated": translated,
            "translated_lang": translate_to
            }

    if request.method == "GET":
        search_results = Language.objects.all()
        return render(request, "pages/homepage.html",{"lang":search_results})
    
    return render(request, "pages/homepage.html", context)
    

def aboutpage_view(request):
    return render(request, "pages/about.html", {})

def servicespage_view(request):
    return render(request, "pages/services.html", {})