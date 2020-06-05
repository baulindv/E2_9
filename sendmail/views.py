from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from .forms import EmailDataForm
from .func import add_email_to_queue, list_email_queue, random_num, EMAIL_TO


def enter_email(request):
    if request.method == 'POST':
        form = EmailDataForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_email_to_queue(cd['email'],
                               cd['subject'],
                               cd['text'],
                               cd['delay'])
            success = True
    else:
        success = False

    form = EmailDataForm(initial={'email': EMAIL_TO if len(EMAIL_TO) > 1 else '',
                                  'subject': f'Тема {random_num(10000000)}',
                                  'text': f'Текст {random_num(10000000)}',
                                  'delay': random_num(60)})

    return render(request,
                  'enter.html',
                  {'form': form,
                   'success': success})


@require_GET
def list_email(request):
    email_queue = list_email_queue()
    return render(request,
                  'list.html',
                  {'email_queue': email_queue})
