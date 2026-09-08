from django.shortcuts import render
from django.core.files.storage import default_storage
from PIL import Image


def upload_image(request):

    image_url = None

    if request.method == "POST":

        uploaded_file = request.FILES.get("image")

        if uploaded_file:

            Image.open(uploaded_file).verify()
            uploaded_file.seek(0)

            file_name = default_storage.save(
                uploaded_file.name,
                uploaded_file
            )

            image_url = default_storage.url(file_name)

    if image_url is None:

        files = default_storage.listdir("")[1]

        if files:
            image_url = default_storage.url(files[0])

    return render(
        request,
        "core/upload.html",
        {"image_url": image_url}
    )