from django.shortcuts import render
from .models import Сomitet
from .forms import ClientForm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import  render_to_string

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about-conference.html')


def advt(request):
    return render(request, 'main/advt.html')


def social_events(request):
    return render(request, 'main/social-events.html')


def comitet(request):
    comitet = Сomitet.objects.all()
    return render(request, 'main/comitet.html', {"comitet": comitet})


def reg(request):
    res = ""
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            res = "Регистрация успешно завершена!"
            msg = EmailMultiAlternatives(subject="test", to=['gulnurs777@gmail.com'])
            txt = render_to_string("main/send_message.html")
            msg.attach_alternative(txt, "text/html")
            msg.send()
            form.save()
        else:
            res = "Данные введены неправильно!"
    form = ClientForm()
    context = {
        'form': form,
        'res': res
    }
    return render(request, 'main/reg.html', context)

def regis(request):

    return render(request, 'main/registration-and-publishing-fees.html')
