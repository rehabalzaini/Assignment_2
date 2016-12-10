from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import entries

# Create your views here.
def show_entries(request):

    if request.method == "POST":
        entries.objects.create(name=request.POST.get("entry_name"),
                            description=request.POST.get("description_entry_name"))

    return render(request, "my_entires.html", {"entries": entries.objects.all()})


def get_entry(request, entry_id):
    try:
        entry = entries.objects.get(id=entry_id)
        return render(request, "detailed_entry.html", {"entry": entry})
    except entries.DoesNotExist:
        raise Http404("We don't have any.")