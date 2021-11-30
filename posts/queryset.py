# Django
from django.db import models


class PostQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(is_public=True)
