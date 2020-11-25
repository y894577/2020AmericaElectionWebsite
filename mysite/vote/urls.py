from django.urls import path
from . import views

urlpatterns = [
    path('state/', views.queryState, name='queryState'),
    path('state/<int:id>', views.queryState, name='queryState'),
    path('candidate/', views.queryCandidate, name='queryCandidate'),
    path('candidate/<int:id>', views.queryCandidate, name='queryCandidate'),
]
