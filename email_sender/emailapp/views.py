# # emailapp/views.py
# from django.core.mail import send_mail
# from django.shortcuts import render
# from .forms import EmailForm

# def send_email(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             recipient = form.cleaned_data['recipient']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             send_mail(subject, message, 'your_email@gmail.com', [recipient])
#             return render(request, 'emailapp/success.html')
#     else:
#         form = EmailForm()
#     return render(request, 'emailapp/send_email.html', {'form': form})



# # Create your views here.

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            recipient_list = [email.strip() for email in recipients.split(',')]
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'your_email@gmail.com', recipient_list)
            return render(request, 'emailapp/success.html')
    else:
        form = EmailForm()
    return render(request, 'emailapp/send_email.html', {'form': form})
