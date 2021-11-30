from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete", views.PostDeleteView.as_view(), name="post-delete"),
    path("<int:pk>/public", views.is_public, name="post-is-public"),
    path("", views.PostCreateView.as_view(), name="post-create"),
]
