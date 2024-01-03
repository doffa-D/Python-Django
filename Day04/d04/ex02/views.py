from django.shortcuts import render
from .forms import my_Form
from django.conf import settings
import datetime

def Django_from(request):
    if request.method == 'POST':
        form = my_Form(request.POST)
        if form.is_valid():
            input = form.cleaned_data['history']
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(settings.LOG_FILE , 'a') as file:
                file.write(f"{time} : {input}\n")
    else:
        form = my_Form()
    history = []
    with open(settings.LOG_FILE , 'r') as file:
        history.append(file.read())
    return render(request, 'indexz.html', {'form': form , 'history': history})