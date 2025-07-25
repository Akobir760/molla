from django.shortcuts import render

# Create your views here.

def register_page_view(request):
    return render(request, template_name="auth/login.html")