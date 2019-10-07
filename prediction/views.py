from django.shortcuts import render
from django.views import View
import requests


class PredictionView(View):
    def get(self, request):
        url = "https://9bhswaqkbk.execute-api.ap-northeast-1.amazonaws.com/salary/prediction"
        params = {'rank': 'S3', 'capacity': 2}
        res = requests.get(url, params=params)
        json_data = res.json()

        return render(request, 'prediction.html', context={
            'salary': json_data['body']
        })
