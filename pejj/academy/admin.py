from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..base.admin import BaseAdmin
from ..base.admin import app_admin_site
from ..base.admin import register
from .models import Classroom
from .models import ClassSchedule
from .models import Enroll
from .models import Trainer


@register(Trainer, app_admin_site)
class TrainerAdmin(BaseAdmin):
    list_display = (
        "id",
        "person",
        "active",
    )
    list_filter = ("active",)
    search_fields = ("person__name",)


@register(ClassSchedule, app_admin_site)
class ClassScheduleAdmin(BaseAdmin):
    list_display = (
        "id",
        "description",
        "weekday",
        "time",
    )
    list_filter = (
        "weekday",
        "time",
    )
    search_fields = ("description",)


@register(Enroll, app_admin_site)
class EnrollAdmin(BaseAdmin):
    list_display = (
        "id",
        "plan",
        "date",
        "person",
    )
    list_filter = ("plan",)
    search_fields = (("person__name", "plan__name"),)


@register(Classroom, app_admin_site)
class ClassroomAdmin(BaseAdmin):
    list_display = (
        "id",
        "date",
        "trainer",
        "display_athletes",
    )
    list_filter = (
        "date",
        "trainer",
    )
    search_fields = (
        "trainer__person__name",
        "athletes__name",
        "athletes__nick",
    )
    date_hierarchy = "created_at"

    def display_athletes(self, obj: Classroom):
        athletes = obj.athletes.all()
        if athletes:
            return format_html(
                "<ul>{}</ul>",
                format_html(
                    "".join(f"<li>{athlete!s}</li>" for athlete in athletes),
                ),
            )
        return format_html("<ul><li>No athletes</li></ul>")

    display_athletes.short_description = _("Athletes")
