from django.db import models
from django.utils.translation import gettext_lazy as _

from pejj.base.mixins import MixinModelCreatedInfo
from pejj.base.mixins import MixinModelUUID


class Trainer(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    person = models.OneToOneField(
        to="base.PEJJPerson",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = _("Trainer")
        verbose_name_plural = _("Trainers")
        db_table = "trainer"


class ClassSchedule(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    class ClassScheduleWeekday(models.IntegerChoices):
        MONDAY = 0, _("Monday")
        TUESDAY = 1, _("Tuesday")
        WEDNESDAY = 2, _("Wednesday")
        THURSDAY = 3, _("Thursday")
        FRIDAY = 4, _("Friday")
        SATURDAY = 5, _("Saturday")
        SUNDAY = 6, _("Sunday")

    description = models.CharField(
        verbose_name=_("Description"),
        max_length=100,
        unique=True,
    )
    weekday = models.PositiveSmallIntegerField(
        verbose_name=_("Weekday"),
        choices=ClassScheduleWeekday.choices,
    )
    time = models.TimeField(
        verbose_name=_("Time"),
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("Class Schedule")
        verbose_name_plural = _("Class Schedules")
        db_table = "class_schedule"


class Enroll(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    date = models.DateField(
        verbose_name=_("Date"),
    )
    person = models.ForeignKey(
        to="base.PEJJPerson",
        verbose_name=_("Person"),
        on_delete=models.DO_NOTHING,
    )
    plan = models.ForeignKey(
        to="base.PEJJPlan",
        verbose_name=_("Plan"),
        on_delete=models.DO_NOTHING,
    )
    schedules = models.ManyToManyField(
        to="academy.ClassSchedule",
        verbose_name=_("Schedules"),
    )

    class Meta:
        verbose_name = _("Enroll")
        verbose_name_plural = _("Enrollment")
        db_table = "enroll"


class Classroom(
    MixinModelUUID,
    MixinModelCreatedInfo,
):
    date = models.DateTimeField(
        verbose_name=_("Date"),
    )
    trainer = models.ForeignKey(
        verbose_name=_("Trainer"),
        to="academy.Trainer",
        on_delete=models.DO_NOTHING,
    )
    class_plan = models.TextField(
        verbose_name=_("Class Plan"),
        null=True,
        blank=True,
    )
    class_performed = models.TextField(
        verbose_name=_("Class Performed"),
        null=True,
        blank=True,
    )
    class_description = models.TextField(
        verbose_name=_("Class Description"),
        null=True,
        blank=True,
    )
    class_photo = models.ImageField(
        verbose_name=_("Class Photo"),
        upload_to="public/",
        null=True,
        blank=True,
    )
    athletes = models.ManyToManyField(
        verbose_name=_("Athlete"),
        to="base.PEJJPerson",
    )

    class Meta:
        verbose_name = _("Classroom")
        verbose_name_plural = _("Classrooms")
        db_table = "classroom"
