from django.shortcuts import render
from django.views.generic import View


def hello_world(request):
    return render(request, 'hello_world.html', {})


class IndexView(View):
    def get(self, request):
        return render(request, 'hello_world2.html', {})
