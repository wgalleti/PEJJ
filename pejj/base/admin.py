from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import PEJJPerson
from .models import PEJJPlan


def register(model, admin_site):
    def decorator(admin_class):
        admin_site.register(model, admin_class)
        return admin_class

    return decorator


class BaseAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, "created_by") and request.user:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class AdminAppSite(AdminSite):
    admin.site.site_header = "PEJJ"
    admin.site.site_title = "PEJJ"


app_admin_site = AdminAppSite(name="app_admin")


@register(PEJJPerson, app_admin_site)
class PEJJPersonAdmin(BaseAdmin):
    list_display = (
        "id",
        "name",
        "nick",
        "document",
        "photo",
    )
    search_fields = (
        "name",
        "nick",
        "document",
    )


@register(PEJJPlan, app_admin_site)
class PEJJPlanAdmin(BaseAdmin):
    list_display = (
        "id",
        "name",
        "times_in_week",
        "number_of_classes",
        "duration_in_months",
        "value",
    )
    list_filter = (
        "number_of_classes",
        "duration_in_months",
    )
    search_fields = ("name",)
