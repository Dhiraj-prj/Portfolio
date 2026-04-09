from django.contrib import admin
from .models import Profile, SkillCategory, Skill, Project, Experience, Achievement, Education

admin.site.site_header = "Dhiraj Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Your Portfolio"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'tagline', 'bio', 'is_available')}),
        ('Photo', {'fields': ('photo', 'photo_url'), 'description': 'Either upload a photo OR paste a direct image URL below. URL is recommended for Railway hosting.'}),
        ('Contact', {'fields': ('email', 'phone', 'location')}),
        ('Social Links', {'fields': ('github', 'linkedin')}),
        ('Resume', {'fields': ('resume', 'resume_url')}),
    )


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2
    fields = ('name', 'order')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ('name', 'icon', 'order')
    list_editable = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'order')
    list_editable = ('featured', 'order')
    list_filter = ('featured',)
    fieldsets = (
        ('Project Info', {'fields': ('title', 'description')}),
        ('Image', {'fields': ('image', 'image_url'), 'description': 'Either upload an image OR paste a direct image URL. URL is recommended.'}),
        ('Tech & Links', {'fields': ('tech_stack', 'github_url', 'live_url')}),
        ('Display', {'fields': ('featured', 'order')}),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date', 'order')
    list_editable = ('order',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'order')
    list_editable = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('level', 'institution', 'gpa', 'year', 'order')
    list_editable = ('order',)
