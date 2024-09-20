from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

from .forms import NameForm, ContactForm


@permission_required("contacts.add_contact")
def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["subject"]
            form.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "contacts/create.html", context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))

    else:
        form = NameForm()

    return render(request, "contacts/name.html", {"form": form})


def thanks(request, name):
    return HttpResponse(f"Obrigado {name}")
