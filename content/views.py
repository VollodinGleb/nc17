from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import *
from django.utils.translation import get_language
from itertools import chain
from .forms import ContactForm
from django.http import HttpResponse
import json
import smtplib
from email.mime.text import MIMEText


class HomeView(CreateView):
    template_name = 'home.html'
    queryset = Section.objects.all()
    form_class = ContactForm

    def form_invalid(self, form):
        return HttpResponse(status=400, content=json.dumps(form.errors))

    def form_valid(self, form):
        msg = """
        Кто-то заполнил форму на сайте)
        Name: {name},
        Email: {email},
        Phone number: {phone_number},
        Message: {message}
        """.format(name=form.instance.name,
                   email=form.instance.email,
                   phone_number=form.instance.phone_number,
                   message=form.instance.text)
        email(subject='Контакт с nc17showballet.com', msg=msg)
        return HttpResponse(status=201)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['initial_section'] = self.queryset.get(name__icontains='initial')
        context['about_section'] = self.queryset.get(name__icontains='about')
        context['photos_section'] = self.queryset.get(name__icontains='photos')
        context['videos_section'] = self.queryset.get(name__icontains='videos')
        context['contacts_section'] = self.queryset.get(name__icontains='contacts')
        context['katya_section'] = self.queryset.get(name__icontains='katya')
        context['anya_section'] = self.queryset.get(name__icontains='anya')
        return context


class AboutView(DetailView):
    template_name = 'about.html'
    model = About

    def get_object(self, queryset=About.objects.all()):
        return queryset.get(language=Constants.LANGUAGE_CODES[get_language()])


class PhotosView(ListView):
    template_name = 'photos.html'

    def get_queryset(self):
        photos = Photo.objects.all()
        videos = Video.objects.filter(show_in_photos=True)
        return sorted(chain(photos, videos),
                      key=lambda obj: obj.order_id)


class VideosView(ListView):
    template_name = 'videos.html'
    queryset = Video.objects.all().order_by('order_id')


class ContactsView(CreateView):
    template_name = 'contacts.html'
    form_class = ContactForm

    def form_invalid(self, form):
        return HttpResponse(status=400, content=json.dumps(form.errors))

    def form_valid(self, form):
        msg = """
        Кто-то заполнил форму на сайте)
        Name: {name},
        Email: {email},
        Phone number: {phone_number},
        Message: {message}
        """.format(name=form.instance.name,
                   email=form.instance.email,
                   phone_number=form.instance.phone_number,
                   message=form.instance.text)
        email(subject='Контакт с nc17showballet.com', msg=msg)
        return HttpResponse(status=201)


class PromotionsView(DetailView):
    template_name = 'promotion.html'
    model = Promotion


def email(from_email='booking@nc17showballet.com',
          to_email='palamarchuk.ann@gmail.com',
          subject="", msg="", password=None):
    if password is None:
        password = 'sonyara123123QQ'
    msg = MIMEText(msg)
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    server = smtplib.SMTP('skm33.hostsila.org', 26)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
