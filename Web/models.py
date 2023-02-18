from django.db import models

class Ranking(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rank = models.IntegerField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='rankings/', null=True, blank=True)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    image = models.ImageField(upload_to='collections/', null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    image = models.ImageField(upload_to='subjects/', null=True, blank=True)

class University(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='universities/', null=True, blank=True)

class Institution(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='institutions/', null=True, blank=True)

class Provider(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='providers/', null=True, blank=True)

class Report(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_profile_picture = models.ImageField(upload_to='authors/', null=True, blank=True)
    publication_date = models.DateField()
    url = models.URLField()
    summary = models.TextField()
    image = models.ImageField(upload_to='reports/', null=True, blank=True)


class Course(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    url = models.URLField()
    course_id = models.CharField(max_length=255)
    workload = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE, null=True, blank=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    
