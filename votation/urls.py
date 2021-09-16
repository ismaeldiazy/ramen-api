from django.urls import path, re_path
from votation.views import (
    ramen_ya_views,
    vote_views,
)

urlpatterns = [
    path('ramenya/', ramen_ya_views.RamenYaList.as_view()),
    path('ramenya/<int:pk>/', ramen_ya_views.RamenYaDetail.as_view()),
    path('vote/', vote_views.VoteList.as_view()),
    path('vote/<int:pk>/', vote_views.VoteDetail.as_view()),
    re_path(r'^vote/(?P<ramen_pk>[0-9])/$', vote_views.VoteList.as_view()),
]