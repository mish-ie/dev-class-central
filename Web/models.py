from django.db import models

class Stream(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    homepage = models.TextField(null=True, blank=True)

class Offering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    exact_dates_known = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    url = models.TextField(null=True, blank=True)

class CourseInstructor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

def trigger_set_created_column(sender, instance, **kwargs):
    if not instance.created:
        instance.created = timezone.now()

models.signals.pre_save.connect(trigger_set_created_column, sender=Offering)
