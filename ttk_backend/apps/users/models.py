from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.utils.translation import gettext_lazy as _

from ttk_backend.core.models.models import AbstractAudit, AbstractChoice


class User(AbstractUser, AbstractAudit):
    """
    Default custom user model for Ttk Backend Backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    # username = None  # type: ignore

    rol = models.ForeignKey(
        'Role',
        verbose_name=_('rol'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    phone = models.CharField(
        _('telefono'),
        max_length=100,
        help_text=_("telefono"),
        blank=True,
        null=True,
        default=None
    )

    cellphone = models.CharField(
        _('celular'),
        max_length=100,
        help_text=_("celular"),
        blank=True,
        null=True,
        default=None
    )

    email = models.EmailField(_('email address'),
                              unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')


class Role(AbstractChoice):
    class Meta:
        db_table = 'roles'
        verbose_name = _('rol')
        verbose_name_plural = _('roles')
