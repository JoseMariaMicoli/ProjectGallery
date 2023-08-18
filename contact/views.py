from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
        try:
            send_mail(subject, message, email, ["cr4sh.dump@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Error: Invalid header found!")
        return redirect('success')
    return render(request, "contact/contact.html", {"form": form})
    
def successView(request):
    return HttpResponse("Success! Thank you for your message. We will respond as soon as possible.")