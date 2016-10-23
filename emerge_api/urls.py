from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^hospitals/$',
        views.HospitalList.as_view(),
        name='hospital-list'),
    url(r'^survey/(?P<pk>(\w+))/$',
        views.SurveyDetail.as_view(),
        name='survey-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]