from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from session.models import Topic, Video, MCQ
from session.serializer import TopicSerializer, VideoSerializer, MCQSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    http_method_names = ['get', 'post', 'delete', "patch"]
    permission_classes = [IsAuthenticated, ]

    # get videos
    @action(detail=True, methods=['get'], url_path='videos', url_name='get_videos')
    def get_videos(self, request, pk=None):
        topic = self.get_object()
        videos = Video.objects.filter(topic=topic)
        return Response(VideoSerializer(videos, many=True).data)

    @action(detail=True, methods=['post'], url_path='videos', url_name='add_video,', permission_classes=[IsAdminUser])
    def add_video(self, request, pk=None):
        topic = self.get_object()
        video = Video.objects.create(**request.data)
        topic.videos.add(video)
        topic.save()
        return Response(VideoSerializer(video).data)
        # update video

    # delete video
    @action(detail=True, methods=['delete'], url_path='videos/(?P<video_id>[^/.]+)', url_name='delete_video',
            permission_classes=[IsAdminUser])
    def delete_video(self, request, pk=None, video_id=None):
        video = Video.objects.get(id=video_id)
        video.delete()
        return Response(status=204)

    # get mcqs
    @action(detail=True, methods=['get'], url_path='mcqs', url_name='get_mcqs')
    def get_mcqs(self, request, pk=None):
        topic = self.get_object()
        mcqs = MCQ.objects.filter(topic=topic)
        return Response(MCQSerializer(mcqs, many=True).data)
