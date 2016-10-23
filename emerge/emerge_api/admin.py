from django.contrib import admin

from .models import \
    (Hospital, Question, Category, Survey,
     Response, AnswerText, AnswerRadio,
     AnswerSelect, AnswerInteger,
     AnswerSelectMultiple)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    empty_value_display = '-empty-'


class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ('category',)
    extra = 0


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, QuestionInline]


class AnswerBaseInline(admin.StackedInline):
    fields = ('question', 'body')
    readonly_fields = ('question',)
    extra = 0


class AnswerTextInline(AnswerBaseInline):
    model = AnswerText


class AnswerRadioInline(AnswerBaseInline):
    model = AnswerRadio


class AnswerSelectInline(AnswerBaseInline):
    model = AnswerSelect


class AnswerSelectMultipleInline(AnswerBaseInline):
    model = AnswerSelectMultiple


class AnswerIntegerInline(AnswerBaseInline):
    model = AnswerInteger


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('survey_uuid', 'hospital', 'created')
    inlines = [AnswerTextInline, AnswerRadioInline, AnswerSelectInline, AnswerSelectMultipleInline, AnswerIntegerInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ('survey', 'created', 'updated', 'survey_uuid')
