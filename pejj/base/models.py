from django.db import models
from django.utils.translation import gettext_lazy as _

from pejj.base.mixins import MixinModelCreatedInfo
from pejj.base.mixins import MixinModelUUID


class PEJJPerson(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        db_index=True,
    )
    nick = models.CharField(
        verbose_name=_("Nick"),
        max_length=100,
        null=True,
        blank=True,
    )
    document = models.CharField(
        verbose_name=_("document"),
        max_length=50,
        null=True,
        blank=True,
        unique=True,
        db_index=True,
    )
    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to="persons/%Y/%m/%d",
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.nick:
            return f"{self.nick} - {self.name}"
        return self.name

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        db_table = "person"


class PEJJPlan(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    name = models.CharField(
        verbose_name=_("Name"),
    )
    times_in_week = models.PositiveSmallIntegerField(
        verbose_name=_("Times in week"),
    )
    number_of_classes = models.PositiveSmallIntegerField(
        verbose_name=_("Number of classes"),
    )
    duration_in_months = models.PositiveSmallIntegerField(
        verbose_name=_("Duration in months"),
    )
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plans")
        db_table = "plan"
