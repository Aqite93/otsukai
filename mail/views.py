from django.shortcuts import render
from django.core.mail import send_mail
# from django.http import HttpResponse
from errand.forms import ErrandIndexFormSet


def send(request):
    print(f'request: {request}')
    subject = "otshukai: You are assigned request of errand!"
    """本文"""
    message = "You have accepted errand."
    """送信元メールアドレス"""
    from_email = "notification@otsukai.com"
    """宛先メールアドレス"""
    # recipient_list = request.POST.get('email')
    recipient_list = [
        "Aqite93@gmail.com"
    ]

    send_mail(subject, message, from_email, recipient_list)
    # return HttpResponse('<h1>email send complete.</h1>')

    formset = ErrandIndexFormSet(request.POST or None)

    return render(request, 'errands_index.html', context={
        'formset': formset,
        'mail': True
    })
