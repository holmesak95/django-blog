#---------------------------------------------------------------------#
# Title: urls.py
# Desc: <Enter Description here>
# Change Log: (Who, When, What)
# <Example Dev, 2030-Jan-01, Created File>
#---------------------------------------------------------------------#
# polling/urls.py

from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"),
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
]
