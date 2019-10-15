from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate
from .forms import UserForm
from .models import User


class LoginView(View):
    def get(self, request):
        form = UserForm()

        return render(request, 'login.html', context={
            'form': form
        })

    def post(self, request):
        form = UserForm(request.POST)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = authenticate(email=email, password=password)
        if user is None:
            return render(request, 'registration/login.html', context={
                'form': form,
                'message': '入力した情報が正しくありません。内容を確認の上、再度入力してください。'
            })

        return redirect(reverse('errand:index'))
