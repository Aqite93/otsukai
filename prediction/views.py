from django.shortcuts import render
from django.views import View
from .forms import PredictionForm
import requests


class PredictionView(View):
    def get(self, request):
        form = PredictionForm()

        return render(request, 'prediction.html', context={
            'form': form
        })

    def post(self, request):
        rank = request.POST.get('rank')
        capacity = int(request.POST.get('capacity'))

        # request aws API gateway of getCSCV
        url = "https://9bhswaqkbk.execute-api.ap-northeast-1.amazonaws.com/salary/prediction"
        params = {'rank': rank, 'capacity': capacity}
        res = requests.get(url, params=params)
        json_data = res.json()

        return render(request, 'prediction_result.html', context={
            'salary': json_data['body']
        })
