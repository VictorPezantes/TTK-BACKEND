from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ttk_backend.apps.users.forms import UserAdminChangeForm, UserAdminCreationForm
from ttk_backend.apps.users.models import Role
from ttk_backend.core.admin import AuditAdminMixin

User = get_user_model()


@admin.register(User)
class UserAdmin(AuditAdminMixin, admin.ModelAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name", "rol")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(Role)
class RoleAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']
