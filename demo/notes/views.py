from django.shortcuts import render, redirect
from .models import note
from .forms import NoteForm

# Create your views here.
def mynote(request):
    items = note.objects.all().order_by("-created_at")
    return render(request, "index.html", {"notes": items})

def adding_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note")
    else:
        form = NoteForm()
    return render(request, "add_notes.html", {"form": form})