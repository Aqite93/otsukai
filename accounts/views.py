from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def logout_view(request):
    logout(request)
    redirect('login.html')


class LoginView(View):
    def post(self, request):
        form = UserForm(request.POST)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        request.session['email'] = email

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'registration/login.html', context={
                'form': form,
                'message': '入力した情報が正しくありません。内容を確認の上、再度入力してください。'
            })

        return redirect(reverse('errand:index'))
        # elif '_singup' in request.POST:
        #     print('--- pushed sing up button! ---')
        #     return redirect(reverse('accounts:singup'))


class SignUp(CreateView):
    model = User
    form_class = UserForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
