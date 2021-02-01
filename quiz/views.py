from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import (
    CommentSerializer, QuizReadSerializer,
    QuizEditSerializer,
)
from .models import (
    Quiz,
)


class QuizViewset(viewsets.ModelViewSet):
    '''
    retrieve:

    create:

    update:

    partial_update:

    destroy:

    edit:

    check:

    '''
    queryset = Quiz.all()
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuizReadSerializer
        else:
            return QuizEditSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['GET'])
    def edit(self, request, *args, **kwargs):
        serializer = QuizEditSerializer(self.get_object())
        return Response(serializer.data, status.status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def check(self, request, *args, **kwargs):
        serializer = QuizEditSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_200_OK) #TODO: need to calculate how many correct asnwers was given and save result 


class CommentViewset(viewsets.ModelViewSet):
    '''
    '''
    serializer_class = CommentSerializer

    def get_quiz(self):
        quiz = get_object_or_404(Quiz, pk=self.kwargs.get('quiz_pk'))
        return quiz

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, quiz=self.get_quiz())
