from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from votation.views import (
    ramen_ya_list
)

urlpatterns = [
    path('ramenya/', ramen_ya_list.RamenYaList.as_view())
]