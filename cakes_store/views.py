from django.shortcuts import render


def index(request):
    context = {
        'Step': 'Number',
    }
    return render(request, 'index.html', context)
