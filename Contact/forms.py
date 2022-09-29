from django import forms

class ContactForm(forms.Form):
	asunto=forms.CharField(label="Asunto", required=True)
	email=forms.EmailField(label="Email", required=True)
	mesage=forms.CharField(label="Mesage", required=True, widget=forms.Textarea)
