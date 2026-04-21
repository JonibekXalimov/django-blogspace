from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name="list"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="update"),
    path("<int:pk>/detail/", ArticleDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete"),
    path("create/", ArticleCreateView.as_view(), name="create"),
]
