from django.urls import path
from .view import SearchResultsView

urlpatterns = [ 
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
