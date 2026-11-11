from django.shortcuts import render
from .models import Career

# Create your views here.

def career(request,slug_urls):
    careers = Career.objects.get(slug=slug_urls)
    context = {'careers': careers}
    return render(request, "career.html", context)