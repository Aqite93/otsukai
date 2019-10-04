from django.shortcuts import render
from django.core.mail import send_mail
# from django.http import HttpResponse
from errand.forms import ErrandIndexFormSet
import requests
import json


def send_mail_via_gmail(request):
    subject = "otshukai: You are assigned request of errand!"
    message = "You have accepted errand."
    from_email = "notification@otsukai.com"
    recipient_list = [
        "Aqite93@gmail.com"
    ]

    send_mail(subject, message, from_email, recipient_list)
    # return HttpResponse('<h1>email send complete.</h1>')


def send_slack():
    requests.post('https://hooks.slack.com/services/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', data=json.dumps({
        'text': u'Notification that you received errand.',
        'username': u'otsukai, inc. ',
        'icon_emoji': u':ghost:',
        'link_names': 1,
    }))


def send(request):
    print(f'request: {request}')
    send_mail_via_gmail(request)
    send_slack()

    formset = ErrandIndexFormSet(request.POST or None)

    return render(request, 'errands_index.html', context={
        'formset': formset,
        'mail': True
    })
