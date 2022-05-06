from django.shortcuts import render


def index(request):
    context = {
        'Step': 'Number',
    }
    return render(request, 'index.html', context)


def reg(request):
    context = {
        'Step': 'Number',
    }

    if request.method == 'POST':
        return render(request, 'index.html', context)
        # form = RegisterUserForm_fiz(request.POST)
        # if form.is_valid():
        #     contract = form.save()
        #     return render(request, 'registration/register_ok.html')
        # else:
        #     return render(request, 'registration/register_fiz.html', {'form': form})
    else:
        return render(request, 'index.html', context)

        # form = RegisterUserForm_fiz()
        # return render(request, 'registration/register_fiz.html', {'form': form})
    # return render(request, 'main/uconstruction.html')
