from rest_framework import serializers

# import models of university app
from .models import MCQ, Topic, Video


# mcq Serializer
class MCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQ
        fields = ['question', 'option1', 'option2', 'option3', 'option4', "topic"]
        extra_kwargs = {
            'topic': {'read_only': True},
            "question": {"read_only": True},
            "option1": {"read_only": True},
            "option2": {"read_only": True},
            "option3": {"read_only": True},
            "option4": {"read_only": True},
        }

    # validation answer must be one of the options
    def validate_answer(self, value):
        if value not in [self.initial_data['option1'], self.initial_data['option2'], self.initial_data['option3'],
                         self.initial_data['option4']]:
            raise serializers.ValidationError("Answer must be one of the options")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['topic'] = instance.topic.name
        return representation


# video Serializer
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'url', 'topic']
        extra_kwargs = {
            'topic': {'read_only': True},
            "name": {"read_only": True},
            "url": {"read_only": True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['topic'] = instance.topic.name
        return representation


# topic Serializer
class TopicSerializer(serializers.ModelSerializer):
    video_count = serializers.SerializerMethodField()
    mcq_count = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['name', "id", "video_count", "mcq_count"]
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def get_video_count(self, obj):
        return obj.video_set.count()

    def get_mcq_count(self, obj):
        return obj.mcq_set.count()
