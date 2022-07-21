from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Task_app.forms import TaskAppForm
from Task_app.models import TaskApp
from random import randrange
from django.core.mail import send_mail


def home(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'index.html')
    else:
        return redirect('ulogin')

# authentication part(closed)
def usignup(request):
	if request.method=="POST":
		un=request.POST.get("un")
		pw1=request.POST.get("pw1")
		pw2=request.POST.get("pw2")
		if pw1==pw2:
			try:
				usr=User.objects.get(username=un)
				return render(request,"usignup.html",{"msg":"user already registered"})
			except User.DoesNotExist:
				usr=User.objects.create_user(username=un,password=pw1)
				usr.save()
				return redirect("ulogin")
		else:
			return render(request,"usignup.html",{"msg":"password did not match"})
	else:
		return render(request,"usignup.html")

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get("un")
		pw=request.POST.get("pw")
		usr=authenticate(username=un,password=pw)
		if usr is not None:
			login(request,usr)
			return redirect("home")
		else:
			return render(request,"ulogin.html",{"msg":"invalid login"})
	else:
		return render(request,"ulogin.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")


# authentication part(closed)
def add_task(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TaskAppForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task = form.save(commit=False)
            task.user = user
            task.save()
            print(task)
            return redirect('home')
        else:
            return render(request, 'add_task.html', {'form': form})
    else:
         return redirect('ulogin')

def view_task(request):
    if request.user.is_authenticated:
        user = request.user
        form = TaskAppForm()
        tasks = TaskApp.objects.filter(user=user).order_by('priority')
        return render(request, 'view_task.html', {'form': form, 'tasks': tasks})
    else:
        return redirect('ulogin')


def delete_task(request, id):
    print(id)
    TaskApp.objects.get(pk=id).delete()
    return redirect('view_task')


def change_status(request, id, status):
    dd = TaskApp.objects.get(pk=id)
    dd.status = status
    dd.save()
    return redirect('view_task')

def info1(request):
	return render(request, 'info1.html')
