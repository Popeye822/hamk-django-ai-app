from django.shortcuts import render, get_object_or_404
from .models import Note


def note_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "core/note_list.html", {"notes": notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "core/note_detail.html", {"note": note})