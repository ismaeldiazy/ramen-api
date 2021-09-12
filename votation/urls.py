from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from votation.views import (
    ramen_ya_views,
    ramen_score_views,
    vote_views,
)

urlpatterns = [
    path('ramenya/', ramen_ya_views.RamenYaList.as_view()),
    path('ramen_score/', ramen_score_views.RamenScoreList.as_view()),
    path('vote/', vote_views.VoteList.as_view()),
]