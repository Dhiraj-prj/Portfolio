from django.shortcuts import render
from .models import Profile, SkillCategory, Project, Experience, Achievement, Education


def index(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    achievements = Achievement.objects.all()
    education = Education.objects.all()

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'projects': projects,
        'experiences': experiences,
        'achievements': achievements,
        'education': education,
    }
    return render(request, 'core/index.html', context)
