from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .queryset import PostQuerySet
from core.models import TimestampedModel, ActiveModel

User = get_user_model()


class Post(TimestampedModel, ActiveModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

    objects = PostQuerySet.as_manager()

    class Meta:
        db_table = "post"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-created_at",)
