from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    # courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='universities/', null=True, blank=True)

class Provider(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    # courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='providers/', null=True, blank=True)
    
    
    
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructor_photos')
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='courses_provided')
    universities = models.ManyToManyField(University, related_name='courses_offered')
    subjects = models.ManyToManyField('Subject', related_name='courses')
    instructors = models.ManyToManyField('Instructor', related_name='courses_taught')
    url = models.URLField(max_length=255)
    workload = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    certificate = models.BooleanField(default=False)
    slug = models.SlugField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    # ranking = models.FloatField(null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    # courses = models.ManyToManyField('Course')
    image = models.ImageField(upload_to='subjects/', null=True, blank=True)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='collections')
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    image = models.ImageField(upload_to='collections/', null=True, blank=True)
    
class Ranking(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rank = models.IntegerField()
    year = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rankings')
    value = models.FloatField()
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.course.title}: {self.value}'
    


class Report(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_profile_picture = models.ImageField(upload_to='author_photos')
    author_bio = models.TextField()
    image = models.ImageField(upload_to='report_images')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reports')
    publication_date = models.DateField()
    url = models.URLField()
    summary = models.TextField()

class Institution(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    courses = models.ManyToManyField('Course')
    logo = models.ImageField(upload_to='institutions/', null=True, blank=True)







