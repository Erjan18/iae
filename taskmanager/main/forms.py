from .models import Client
from django.forms import ModelForm, TextInput,  Select, Textarea, EmailInput, NumberInput


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "position",
            "theme",
            "type",
            "format",
            "company",
            "status",
            "email",
            "tel",
            "city",
            "country",
            "discription"
        ]

        widgets = {
            "name": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "position": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "type": Select(),
            "format": Select(),
            "theme": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "company": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "status": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле",

            }),
            "email": EmailInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "tel": NumberInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле, номер телефона должен быть в международном формате без '+'"
            }),
            "city": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "country": TextInput(attrs={
                "type": "text",
                "placeholder": "Заполните поле"
            }),
            "discription": Textarea(attrs={
                "placeholder": "Заполните поле"
            })
        }