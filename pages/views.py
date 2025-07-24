from django.shortcuts import redirect, render
from django.contrib import messages

from pages.forms import ContactModelForm


def home_page_view(request):
    return render(request, template_name='index-1.html')


def contact_page_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message has been send to admins ✅"
                )
        else:
            messages.error(request, "Please, check your data ❌")
        return redirect('pages:contact')
    else:
        return render(request, 'pages/contact-2.html')