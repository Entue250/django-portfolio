from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage

# Create your views here.

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        reason = request.POST.get("reason")
        message = request.POST.get("message")
        
        # Save the data to the database
        ContactMessage.objects.create(name=name, email=email, reason=reason, message=message)
        
        # Return success response
        return JsonResponse({"success": True, "message": "Message Sent Successfully"})
    
    return render(request, 'portfolio/contact.html')
