from django.urls import path

from . import views

# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


# GENERIC VIEWS SYSTEM
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the 2 generic views below.
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
