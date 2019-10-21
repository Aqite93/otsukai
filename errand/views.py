from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ErrandIndexFormSet


class ErrandIndexView(LoginRequiredMixin, View):
    def get(self, request):
        formset = ErrandIndexFormSet(request.POST or None)

        return render(request, 'errands_index.html', context={
            'formset': formset
        })


class ErrandRegisterView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, 'errands_register.html', context={
        })

    def post(self, request):
        print(request.POST)
        return render(request, 'errands_register.html', context={
        })
