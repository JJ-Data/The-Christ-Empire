from django.shortcuts import render, get_object_or_404
from .models import Program

def home(request):
    programs = Program.objects.all()
    return render(request, 'index.html', {'programs':programs})

def about(request):
   return render(request, 'about.html')

def program(request):
   return render(request, 'program.html')

def contact(request):
   return render(request, 'contact.html')

def gallery(request):
   return render(request, 'gallery.html')
