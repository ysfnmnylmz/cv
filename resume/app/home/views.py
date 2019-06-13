from django.shortcuts import render
from .models import PersonalInfo, Section, FooterText, Social


def home(request):
    personalinfo = PersonalInfo.objects.first()
    sections = Section.objects.all()
    footertexts = FooterText.objects.all()
    socials = Social.objects.all()
    payload = {
        'personalinfo': personalinfo,
        'sections': sections,
        'footertexts': footertexts,
        'socials': socials,
    }
    return render(request, 'index.html', payload)
