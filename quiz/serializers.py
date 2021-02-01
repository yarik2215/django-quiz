from rest_framework import serializers

from .models import Quiz, Question, Answer, Comment


class AnswerReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ['text']


class AnswerEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionReadSerializer(serializers.ModelSerializer):
    answers = AnswerReadSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionEditSerializer(serializers.ModelSerializer):
    answers = AnswerEditSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuizReadSerializer(serializers.ModelSerializer):
    question = QuestionReadSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['']


class QuizEditSerializer(QuizReadSerializer):
    questions = QuestionEditSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
