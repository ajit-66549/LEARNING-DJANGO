from django.shortcuts import render
from .models import note

# Create your views here.
def mynote(request):
    items = note.objects.all()
    return render(request, "index.html", {"notes": items})