from django.shortcuts import render
from django.views import View
from .forms import ErrandIndexFormSet


class ErrandIndexView(View):
    def get(self, request):
        formset = ErrandIndexFormSet(request.POST or None)

        return render(request, 'errands_index.html', context={
            'formset': formset
        })
