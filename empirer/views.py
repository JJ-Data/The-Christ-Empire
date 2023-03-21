from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Program, Weekly, Live
from .forms import WeeKlyForm, LiveForm


def loginPage(request):

   if request.method == "POST":
      username = request.POST['username'].lower()
      password = request.POST['password']

      try:
         user = User.objects.get(username=username)
      except:
         messages.error(request, "username does not exist")

      user = authenticate(request, username=username, password=password)

      if user is not None:
         login(request, user)
         messages.success(request, "login successful!")
         return redirect("home")
      else:
         messages.error(request, "username OR password is incorrect")

   return render(request, "login.html")

@login_required()
def logoutUser(request):
   logout(request)
   messages.info(request, "User was logged out")
   return redirect("login")


def home(request):
   #  programs = Program.objects.all()
   programs = Weekly.objects.all()[:3]
   context = {"programs": programs}

   return render(request, 'index.html', context)

def about(request):
   return render(request, 'about.html')

def program(request):
   live_program = Live.objects.first()
   context = {"live_program": live_program}
   return render(request, 'program.html', context)

def contact(request):
   return render(request, 'contact.html')

def gallery(request):
   return render(request, 'gallery.html')

@login_required()
def programsList(request):
   weekly = Weekly.objects.all()[:10]
   live = Live.objects.all()[:5]
   context = {"weekly":weekly, "live":live}

   return render(request, "programs_list.html", context)

@login_required()
def decision(request):
   return render(request, "decision.html")

@login_required()
def createWeekly(request):
   page = "week"

   form = WeeKlyForm()
   if request.method == "POST":
      form = WeeKlyForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, "program was successfully created!")
         return redirect("decision")

   context = {"page":page, "form": form}
   return render(request, "program_form.html", context)

@login_required()
def updateWeekly(request, pk):
   weekly_program = Weekly.objects.get(id=pk)
   form = WeeKlyForm(instance=weekly_program)

   if request.method == "POST":
      form = WeeKlyForm(request.POST, instance=weekly_program)
      if form.is_valid():
         form.save()
         messages.success(request, "program was successfully updated!")
         return redirect("programs_list")

   context = {"form":form}
   return render(request, "program_form.html", context)

@login_required()
def deleteWeekly(request, pk):
   weekly_program = Weekly.objects.get(id=pk)
   if request.method == "POST":
      weekly_program.delete()
      messages.success(request, "program deleted")
      return redirect("programs_list")

   context = {"object": weekly_program}
   return render(request, "delete_template.html", context)  

@login_required()
def createLive(request):
   page = "live" 

   form = LiveForm()
   if request.method == "POST":
      form = LiveForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, "program was successfully created!")
         return redirect("program")

   context = {"page":page, "form": form}
   return render(request, "program_form.html", context)

@login_required()
def updateLive(request, pk):
   weekly_program = Live.objects.get(id=pk)
   form = LiveForm(instance=weekly_program)

   if request.method == "POST":
      form = LiveForm(request.POST, instance=weekly_program)
      if form.is_valid():
         form.save()
         messages.success(request, "program was successfully updated!")
         return redirect("program")

   context = {"form":form}
   return render(request, "program_form.html", context)

@login_required()
def deleteLive(request, pk):
   weekly_program = Live.objects.get(id=pk)
   if request.method == "POST":
      weekly_program.delete()
      messages.success(request, "program deleted!")
      return redirect("programs_list")

   context = {"object": weekly_program}
   return render(request, "delete_template.html", context)  


def read_file(request):
    f = open('52B0311E4A32747D48B4673CFBB46465.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
