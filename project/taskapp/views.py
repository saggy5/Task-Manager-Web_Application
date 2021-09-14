from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TaskForm

def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("user_login")

def create(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			tas =request.POST.get("task")
			data = TaskModel(task=tas, owner=request.user)
			data.save()		
			fm = TaskForm()
			return render(request,"create.html",{"fm":fm,"msg":"Task is added"})	
		else:
			fm = TaskForm()
			return render(request,"create.html",{"fm":fm})
	else:
		return redirect("user_login")

def viewtask(request):
	if request.user.is_authenticated:
		data = TaskModel.objects.filter(owner=request.user)
		return render(request,"viewtask.html",{"data":data})
	else:
		return redirect("user_login")


def delete(request,id):
	d = TaskModel.objects.get(task_no=id)
	d.delete()
	return redirect("viewtask")
