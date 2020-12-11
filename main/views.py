from django.shortcuts import render, redirect
from .models import EmailSent
from main.services.EmailService import EmailService


# Create your views here.
def homepage(request):

    context = {
        'emails': EmailSent.objects.all()
    }
    return render(request,
                  'main/home.html',
                  context)

def search(request):
    if request.method == "GET":
        form = request.GET.get('q')

        return render(request,
                      'main/home.html',
                      {'tutorials': EmailSent.objects.filter(emailSent_content__contains=f'{form}'),
                       'count':EmailSent.objects.filter(emailSent_content__contains=f'{form}').count()}
                      )

def email(request):
    if request.method == "GET":
        form = EmailSent()
        form.email_body = request.GET.get("message")
        form.contact_name = request.GET.get("contact")
        form.contact_email = request.GET.get("email")
        if form.is_valid():
            email_request = EmailService(form)

            email_request.send_email_ssl()

    return redirect('/')

def test(request):
    return render(request,
                  'main/test.html')