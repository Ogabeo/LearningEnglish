from django.db import models
from apps.base.models import BaseModel
# Create your models here.

class CourseCategory(BaseModel):
    title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) :
        return self.title

class Course(BaseModel):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL,null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    cost= models.CharField(max_length=10)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    
    


class Instructor(BaseModel):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='instructors', null=True, blank=True)
    instagram_site= models.CharField(max_length=100)
    youtube_site = models.CharField(max_length=100)
    telegram_site = models.CharField(max_length=100)
    about_instructor = models.TextField()

    def __str__(self):
        return self.name


