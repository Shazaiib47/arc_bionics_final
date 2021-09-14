from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return to the index page """

    return render(request, 'home/index.html')


def contact(request):
    """This will return the contact page 
    and sends the contact form info to the database"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.subject = request.POST['subject'],
            form.message = request.POST['message'],
            form.email = request.POST['email'],
            form.save()
            user_email = ''.join(form.email)
            messages.success(request, f"Thanks {user_email}, Your query has been sent.\
                                        Arc Bionics will be in touch with you.")
            return redirect('home')
        else:
            messages.error(request,'Error: Something has gone wrong, try again later')
            return redirect('home')
    else:
        form = ContactForm()
  
    template = 'home/contact_page.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
