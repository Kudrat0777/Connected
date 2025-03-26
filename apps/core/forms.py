from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Телефон", max_length=20)
    service = forms.CharField(label="Услуга")   ## нужео добавить SERVICE_CHOICES
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)
    
    def send_email(self):
        subject = f"Новая заявка от {self.cleaned_data['name']}"
        message = f"""
            Услуга: {self.cleaned_data['service']}
            Телефон: {self.cleaned_data['phone']}
            Сообщение: {self.cleaned_data['message']}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ["kudratsultanbaev06@yandex.ru"],
            fail_silently=False,
        )
    