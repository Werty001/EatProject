from django.shortcuts import render
from django.core.mail import send_mail
from Contact.forms import ContactForm

# Create your views here.
def Contact(request):
	if request.method==("POST"):
		myForm=ContactForm(request.POST)
		if myForm.is_valid():
			infoForm=myForm.cleaned_data
			send_mail(infoForm["asunto"],infoForm["mesage"],infoForm.get("email",''),["an_ruggero@hotmail.com"],)
		return render (request, "Contact/Thanks")
	else:  
		myForm=ContactForm()
	return render(request, "Contact/ContactForm",{"form":myForm})
