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
        print(form)

        return render(request,
                      'main/home.html',
                      {'tutorials': EmailSent.objects.filter(EmailSent__contains=f'{form}'),
                       'count':EmailSent.objects.filter(message__contains=f'{form}').count()}
                      )

def email(request):
    if request.method == "POST":
        form = EmailSent()
        form.message = request.POST['message']
        form.mail_sender = request.POST['email']
        form.mail_recipient  = "folzieds@gmail.com"
        form.contact_name = request.POST['contact']
        form.subject = f"{request.POST['contact']} {request.POST['email']}"

        if form.is_valid():
            email_request = EmailService(form)

            email_request.send_email_ssl()

        form.save()

    return redirect('/')

def test(request):
    return render(request,
                  'main/test.html')