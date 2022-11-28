#---------------------------------------------------------------------#
# Title: urls.py
# Desc: <Enter Description here>
# Change Log: (Who, When, What)
# <Example Dev, 2030-Jan-01, Created File>
#---------------------------------------------------------------------#
# polling/urls.py

from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="poll_index"),
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
]