from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Survey(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.name

    def questions(self):
        if self.pk:
            return Question.objects.filter(survey=self.pk)
        else:
            return None


class Hospital(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    phone_regex = RegexValidator(regex=r'\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*',
                                 message="Phone number must be entered in the format:"
                                         " '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], null=True, max_length=15)
    address = models.CharField(max_length=256, null=True)
    business_hours = models.CharField(max_length=10, null=True)
    survey = models.ForeignKey(Survey, blank=True, null=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=400)
    survey = models.ForeignKey(Survey)

    @property
    def __str__(self):
        return self.name


def validate_list(value):
    """takes a text value and verifies that there is at least one comma """
    values = value.split(',')
    if len(values) < 2:
        raise ValidationError("The selected field requires an associated list of choices. "
                              "Choices must contain more than one item.")


class Question(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'

    QUESTION_TYPES = (
        (TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT, 'select'),
        (SELECT_MULTIPLE, 'Select Multiple'),
        (INTEGER, 'integer'),
    )

    text = models.TextField()
    required = models.BooleanField()
    category = models.ForeignKey(Category, blank=True, null=True, )
    survey = models.ForeignKey(Survey)
    question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
    choices = models.TextField(blank=True,
                               null=True,
                               help_text='if the question type is "radio," "select," or'
                                         ' "select multiple" provide a comma-separated list '
                                         'of options for this question .')

    def save(self, *args, **kwargs):
        if (self.question_type == Question.RADIO or self.question_type == Question.SELECT
           or self.question_type == Question.SELECT_MULTIPLE):
            validate_list(str(self.choices))
        super(Question, self).save(*args, **kwargs)

    def get_choices(self):
        """ parse the choices field and return a tuple formatted appropriately
        for the 'choices' argument of a form widget."""
        choices = self.choices.split(',')
        choices_list = []
        for c in choices:
            c = c.strip()
            choices_list.append((c, c))
        choices_tuple = tuple(choices_list)
        return choices_tuple

    def __str__(self):
        return self.text


class Response(models.Model):
    # a response object is just a collection of questions and answers with a
    # unique interview uuid
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey)
    hospital = models.ForeignKey(Hospital)
    patient = models.CharField('Name of Patient', max_length=400)
    conditions = models.TextField('Conditions during interview', blank=True, null=True)
    comments = models.TextField('Any additional Comments', blank=True, null=True)
    survey_uuid = models.CharField("Interview unique identifier", max_length=36)

    def __unicode__(self):
        return "response %s" % self.interview_uuid


class AnswerBase(models.Model):
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AnswerText(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerRadio(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelect(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelectMultiple(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerInteger(AnswerBase):
    body = models.IntegerField(blank=True, null=True)