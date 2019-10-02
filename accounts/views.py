from django.shortcuts import render
from .models import User
from django.views import View
from .forms import UserForm


class LoginView(View):
    def get(self, request):
        form = UserForm()

        return render(request, 'login.html', context={
            'form': form
        })
