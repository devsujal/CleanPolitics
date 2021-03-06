from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, desc = desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

def canada(request):
    return render(request, 'canada.html')

def india(request):
    return render(request, 'india.html')
