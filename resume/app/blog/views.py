from django.shortcuts import render
from resume.app.home.models import PersonalInfo, Section
from .models import Post


def blog(request):
    personalinfo = PersonalInfo.objects.first()
    sections = Section.objects.all()
    posts = Post.objects.all()
    payload = {
        'personalinfo': personalinfo,
        'sections': sections,
        'posts': posts
    }
    return render(request, 'blog.html', payload)
