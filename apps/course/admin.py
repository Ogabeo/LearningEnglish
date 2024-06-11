from django.contrib import admin
from .models import Instructor, Course, CourseCategory
from django.utils.html import mark_safe

# Register your models here.
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'created_at')
    list_display_links=('id', 'title')
    
@admin.register(Instructor)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'youtube_site', 'telegram_site',)
    list_display_links = ('id', 'name', 'course', 'youtube_site', )
    search_fields=('name', 'course',)
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'cost', 'number_of_students',   )
    list_display_links = ('id', 'title', 'category',)
    search_fields=('category',)
    list_editable=('cost', 'number_of_students',)
    prepopulated_fields={'slug':('title',)}

    def display_icon(self, obj:Course):
        return mark_safe(f'<img src="{obj.course_image.url}" width="150" />')
    
    display_icon.short_description = 'Icon'


 