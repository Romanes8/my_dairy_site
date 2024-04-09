from django.shortcuts import render, redirect
from .models import Dairy_strings
from .forms import Dairy_stringsForm


def dairy(request):
    strings = Dairy_strings.objects.order_by('-date')
    return render(request, 'dairy/dairy.html', {'strings': strings})


def add(request):
    error = ''
    if request.method == 'POST':
        form = Dairy_stringsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dairy')
        else:
            error = 'Неверный ввод'

    form = Dairy_stringsForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'dairy/add.html',data )
