from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ["user"]

        widgets = {

            "age": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none",
                "placeholder": "Enter your age"
            }),

            "gender": forms.Select(attrs={
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none"
            }),

            "height": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none",
                "placeholder": "Height in cm"
            }),

            "weight": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none",
                "placeholder": "Weight in kg"
            }),

            "medical_conditions": forms.Textarea(attrs={
                "rows": 4,
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none resize-none",
                "placeholder": "Diabetes, asthma, hypertension..."
            }),

            "injuries": forms.Textarea(attrs={
                "rows": 4,
                "class": "w-full rounded-xl border border-gray-300 p-3 focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none resize-none",
                "placeholder": "Back pain, knee injury..."
            }),

            "is_pregnant": forms.CheckboxInput(attrs={
                "class": "h-5 w-5 rounded text-teal-600 focus:ring-teal-500"
            })

        }