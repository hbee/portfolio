from django.shortcuts import render
from experiences.models import exp

def HomeView(request):
    exps = exp.objects.all()
    context = {
        'exps' : exps
    }
    return render(request, 'experiences/home.html', context)
