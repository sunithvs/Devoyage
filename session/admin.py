from django.contrib import admin

# Register your models here.

from .models import MCQ, Topic, Video


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    search_fields = ['name', ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'topic']
    list_filter = ['name', 'url', 'topic']
    search_fields = ['name', 'url', 'topic']


@admin.register(MCQ)
class MCQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'topic']
    list_filter = ['topic']
    search_fields = ['question', 'answer', 'topic']
