from django.shortcuts import render, get_object_or_404
from .models import Airport_data

def index(request):
    results = Airport_data.objects.all()
    return render(request, "index.html", {"data":results})


def airport(request, pk):
    book = get_object_or_404(Airport_data, pk)
    results = Airport_data.objects.all()
    context =  {"data":results,
                 }
    return render(request, "airport.html", context)




def contact(request):
    return render(request, "contact.html")