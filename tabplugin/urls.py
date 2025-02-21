from django.conf import settings
from django.urls import re_path
from .views import MyTabView


urlpatterns = (
    re_path(
        r'courses/{}/chat$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        MyTabView.as_view(),
        name='mytab_view',
    ),
)
