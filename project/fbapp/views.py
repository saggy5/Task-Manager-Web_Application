from django.shortcuts import render,redirect
from .forms import FbForm
from .models import FbModel 


def feedback(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			na = request.POST.get("name")
			num =request.POST.get("number")
			fb = request.POST.get("feedback")
			data = FbModel(name=na,number=num,feedback=fb)
			data.save()
			fm = FbForm()
			return render(request,"feedback.html",{"fm":fm,"msg":"Thank you for your feedback"})

		else:
			fm = FbForm()
			return render(request,"feedback.html",{"fm":fm})
	else:
		return redirect("user_login")

	
