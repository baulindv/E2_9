from django import forms

from .func import random_num


class EmailDataForm(forms.Form):
    email = forms.EmailField(label='Адресат',
                             required=True)
    subject = forms.CharField(max_length=50,
                              label='Тема',
                              required=True)
    text = forms.CharField(max_length=1000,
                           widget=forms.Textarea,
                           label='Текст')
    delay = forms.IntegerField(label='Отсрочка отправки, сек',
                               required=True)
