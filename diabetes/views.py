from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .ml_models import get_prediction


def index(request):
    # return HttpResponse("hello diabetes web")
    context = {
        'status': 'Input test results'
    }
    return render(request, 'diabetes/index.html', context)


def predict(request):
    context = {
        'status': 'Input test results'
    }
    if request.method == 'POST':
        prediction = get_prediction(request.POST)
        context = {
            'status': f"Prediction = {prediction}"
        }
        features = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
               "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    
        for f in features:
            if f in request.POST:
                context[f] = request.POST[f]
                
        return render(request, 'diabetes/index.html', context)
    return render(request, 'diabetes/index.html', context)
