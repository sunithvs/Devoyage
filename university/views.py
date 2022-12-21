from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from university.models import University, Feedback, Course, Gallery
from university.serializer import UniversitySerializer, FeedbackSerializer, CourseSerializer, GallerySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    http_method_names = ['get', 'post', 'delete', "patch"]
    permission_classes = [IsAuthenticated, ]

    # get feedbacks
    @action(detail=True, methods=['get'], url_path='feedbacks', url_name='get_feedbacks')
    def get_feedbacks(self, request, pk=None):
        university = self.get_object()
        feedbacks = Feedback.objects.filter(university=university)
        return Response(FeedbackSerializer(feedbacks, many=True).data)

    @action(detail=True, methods=['post'], url_path='feedbacks', url_name='add_feedback')
    def add_feedback(self, request, pk=None):
        university = self.get_object()
        feedback = Feedback.objects.create(user=request.user, **request.data)
        university.feedbacks.add(feedback)
        university.save()
        return Response(FeedbackSerializer(feedback).data)
        # update feedback

    # delete feedback
    @action(detail=True, methods=['delete'], url_path='feedbacks/(?P<feedback_id>[^/.]+)', url_name='delete_feedback')
    def delete_feedback(self, request, pk=None, feedback_id=None):
        feedback = Feedback.objects.get(id=feedback_id)
        if feedback.user == request.user:
            feedback.delete()
            return Response(status=204)
        else:
            return Response(status=403)

    # get courses
    @action(detail=True, methods=['get'], url_path='courses', url_name='get_courses')
    def get_courses(self, request, pk=None):
        university = self.get_object()
        courses = Course.objects.filter(university=university)
        return Response(CourseSerializer(courses, many=True).data)

    @action(detail=True, methods=['post'], url_path='courses', url_name='add_course')
    def add_course(self, request, pk=None):
        university = self.get_object()
        course = Course.objects.create(**request.data)
        university.courses.add(course)
        university.save()
        return Response(CourseSerializer(course).data)
        # update course

    @action(detail=True, methods=['patch'], url_path='courses/(?P<course_id>[^/.]+)', url_name='update_course')
    def update_course(self, request, pk=None, course_id=None):
        university = self.get_object()
        course = Course.objects.get(id=course_id)
        course.name = request.data['name']
        course.description = request.data['description']
        course.image = request.data['image']
        course.duration = request.data['duration']
        course.intake = request.data['intake']
        course.save()
        return Response(CourseSerializer(course).data)

    @action(detail=True, methods=['delete'], url_path='courses/(?P<course_id>[^/.]+)', url_name='delete_course')
    def delete_course(self, request, pk=None, course_id=None):
        course = Course.objects.get(id=course_id)
        course.delete()
        return Response(CourseSerializer(course).data)

    # get gallery
    @action(detail=True, methods=['get'], url_path='gallery', url_name='get_gallery')
    def get_gallery(self, request, pk=None):
        university = self.get_object()
        gallery = university.gallery
        return Response(GallerySerializer(gallery, many=True).data)

    @action(detail=True, methods=['post'], url_path='gallery', url_name='add_gallery')
    def add_gallery(self, request, pk=None):
        university = self.get_object()
        gallery = Gallery.objects.create(**request.data)
        university.gallery.add(gallery)
        university.save()

        return Response(GallerySerializer(gallery).data)
