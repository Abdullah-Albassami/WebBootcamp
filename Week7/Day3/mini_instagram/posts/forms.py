from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["username", "description", "image"]

        widgets = {
            "image": forms.FileInput(),
        }

    def clean_image(self):
        image = self.cleaned_data.get("image")

        allowed_extensions = ["jpg", "jpeg", "png"]

        extension = image.name.split(".")[-1].lower()

        if extension not in allowed_extensions:
            raise forms.ValidationError(
                "Only JPG, JPEG, and PNG files are allowed."
            )

        return image