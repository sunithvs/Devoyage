from django.contrib import admin
from .models import University, Feedback, Course, Gallery, Image


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'nirf_rank', 'n_u_p', 'affiliations', 'facilities']
    list_filter = ['name', 'nirf_rank', 'n_u_p', 'affiliations', 'facilities']
    search_fields = ['name', 'nirf_rank', 'n_u_p', 'affiliations', 'facilities']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'heading', 'message', 'date']
    list_filter = ['user', 'heading', 'message', 'date']
    search_fields = ['user', 'heading', 'message', 'date']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'duration', 'intake']
    list_filter = ['name', 'description', 'image', 'duration', 'intake']
    search_fields = ['name', 'description', 'image', 'duration', 'intake']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    search_fields = ['name', ]
