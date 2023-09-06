from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Aulia Rizqi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)