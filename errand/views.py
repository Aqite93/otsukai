from django.shortcuts import render
from django.views import View
from .models import Errand
from .forms import ErrandIndexForm


class ErrandIndexView(View):
    def get(self, request):
        errands = Errand.objects.all()
        form = ErrandIndexForm(errands)

        return render(request, 'errands_index.html', context={
            'form': form
        })
