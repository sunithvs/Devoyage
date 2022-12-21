
from rest_framework import serializers

# import models of university app
from university.models import University, Feedback, Course, Image, Gallery


#  feedback Serializer
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        create_fields = ('user', 'heading', 'message')
        fields = ['user', 'heading', 'message', 'date']
        extra_kwargs = {
            'user': {'read_only': True},
            'university': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'name']


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['name', 'images']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description', 'image', 'duration', 'intake']


class UniversitySerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = University
        #         fields of Model University
        fields = (
            'id', 'name', 'description', 'nirf_rank', 'n_u_p', 'affiliations', 'facilities',
            'feedbacks', 'courses', 'gallery')
        extra_kwargs = {
            'id': {'read_only': True},
        }
