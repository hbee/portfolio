from django.shortcuts import render, get_object_or_404
from experiences.models import exp

def HomeView(request):
    exps = exp.objects.all()
    context = {
        'exps' : exps,
    }
    return render(request, 'experiences/home.html', context)

def DetailView(request, exp_id):
    exp_detail = get_object_or_404(exp, pk=exp_id)
    context = {
        'exp': exp_detail,
    }
    return render(request, 'experiences/detail.html', context)