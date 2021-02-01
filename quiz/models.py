from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


def create_path(instance, filename):
    return f'user-{instance.id}.png'


class CustomUser(AbstractUser):
    image = models.ImageField(_('image'), help_text=_('User avatar'), upload_to=create_path)
    birth_date = models.DateField(_('birth date'))
    info = models.TextField(_('info'), help_text=_('Users aditional information'))
    results = models.ManyToManyField('Quiz', through='QuizResults')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class QuizResults(models.Model):
    '''
    User profile for storring quiz results. Create new instance for attempt.
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    answers = models.PositiveIntegerField(_('answers'))
    correct_answers = models.PositiveIntegerField(_('correct answers'))
    created_at = models.DateTimeField(_('created'), auto_now_add=True)


class Quiz(models.Model):
    '''
    Store questions with answers, owner of the quiz and comments.
    '''

    title = models.CharField(_('title'), max_length=255, db_index=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('owner'), related_name='quizes')


class Question(models.Model):
    '''
    Question for quiz.
    Question must have 1 correct answer.
    '''

    text = models.TextField(_('text'))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('quiz'), related_name='questions')


class Answer(models.Model):
    '''
    Answer for question.
    Can be correct or incorrect.
    '''

    text = models.TextField(_('text'))
    is_correct = models.BooleanField(_('correct'), help_text=_('Marks that this is correct answer or no'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('question'), related_name='answers')


class Comment(models.Model):
    '''
    Store comment for the quiz.
    Only authorized users can add comments.
    '''

    text = models.TextField(_('comment'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('owner'), related_name='comments')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='comments')
