from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):

    # User submitted the form
    if request.method == "POST":

        form = ContactForm(request.POST)

        # Run Django validation
        if form.is_valid():

            print(form.cleaned_data)

            return redirect("feedback:thank_you")

    # User opened the page normally
    else:
        form = ContactForm()

    return render(request, "feedback/contact.html", {"form": form})


def thank_you(request):

    return render(request, "feedback/thank_you.html")