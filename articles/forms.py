from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("comments",)
        labels = {
            "comments": "Izoh",
        }
        widgets = {
            "comments": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Fikringizni yozing...",
                }
            )
        }
