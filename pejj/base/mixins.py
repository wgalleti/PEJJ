import uuid

from django.db import models


class MixinModelBase(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, "name"):
            return self.name

        return f"{self.id}"


class MixinModelUUID(MixinModelBase):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class MixinModelCreatedInfo(MixinModelBase):
    created_by = models.ForeignKey(
        to="users.User",
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_created",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
