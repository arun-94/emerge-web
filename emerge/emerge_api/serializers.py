from rest_framework import serializers

from .models import Hospital, Survey, Question, Category

HOSPITAL_FIELDS = ('id',
                   'created',
                   'name',
                   'latitude',
                   'longitude',
                   'contact',
                   'address',
                   'business_hours',
                   'survey')

SURVEY_FIELDS = ('name',
                 'description',
                 'questions')

QUESTION_FIELDS = ('text',
                   'category',
                   'required',
                   'question_type',
                   'choices')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class QuestionSerializer(serializers.ModelSerializer):
    category  = CategorySerializer()

    class Meta:
        model  = Question
        fields = QUESTION_FIELDS


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    survey = serializers.HyperlinkedRelatedField(read_only=True,
                                                 view_name='survey-detail')

    class Meta:
        model  = Hospital
        fields = HOSPITAL_FIELDS


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model  = Survey
        fields = SURVEY_FIELDS
