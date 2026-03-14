from django.urls import path
from .views import note_list, note_detail

urlpatterns = [
    path("", note_list, name="note_list"),
    path("note/<int:note_id>/", note_detail, name="note_detail"),
]