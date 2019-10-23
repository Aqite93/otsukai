from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from .forms import ErrandIndexFormSet, ErrandRegisterForm


class ErrandIndexView(LoginRequiredMixin, View):
    def get(self, request):
        print('--- errand index view start ---')
        formset = ErrandIndexFormSet()

        return render(request, 'errands_index.html', context={
            'formset': formset
        })


class ErrandRegisterView(LoginRequiredMixin, View):
    def get(self, request):
        print('--- errand register(GET request) view start ---')
        form = ErrandRegisterForm(request.POST or None)
        return render(request, 'errands_register.html', context={
            'form': form
        })

    def post(self, request):
        print('--- errand register(POST request) view start ---')
        print(request.POST)

        errand_register_form = ErrandRegisterForm(request.POST, request.FILES)

        if errand_register_form.is_valid():
            print('--- successed form valid ---')
            errand = errand_register_form.save(commit=False)
            errand.user = User.objects.get(pk=1)
            errand.save()

            formset = ErrandIndexFormSet(request.POST or None)

            return render(request, 'errands_index.html', context={
                "from": formset
            })
        else:
            print('--- failed form valid ---')
            print(errand_register_form.errors)
            return render(request, 'errands_register.html', context={
                "from": errand_register_form
            })
