from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label="Name"
    )

    email = forms.EmailField(
        label="Email"
    )

    message = forms.CharField(
        widget=forms.Textarea,
        label="Message"
    )

    rating = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=5,
        label="Rating (1-5)"
    )

    # Custom validation for the message field
    def clean_message(self):

        message = self.cleaned_data["message"]

        if len(message.strip()) < 20:
            raise forms.ValidationError(
                "Message must be at least 20 characters."
            )

        return message