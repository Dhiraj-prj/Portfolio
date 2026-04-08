from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Dhiraj Parajuli")
    tagline = models.CharField(max_length=200, default="BCA Student & Freelance Developer")
    bio = models.TextField(default="Motivated and enthusiastic BCA student with strong technical and problem-solving skills, building web platforms, mental health tools, and civic tech.")
    location = models.CharField(max_length=100, default="Itahari, Nepal")
    email = models.EmailField(default="Parajulidhiraj00@gmail.com")
    phone = models.CharField(max_length=20, default="9815373314")
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default="⚡")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma separated: Django, Python, SQLite")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_stack_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, default="Present")
    description = models.TextField(help_text="Use newlines to separate bullet points")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} @ {self.organization}"

    def get_bullets(self):
        return [b.strip() for b in self.description.split('\n') if b.strip()]


class Achievement(models.Model):
    icon = models.CharField(max_length=10, default="🏆")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Education(models.Model):
    level = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    gpa = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.level} - {self.institution}"
