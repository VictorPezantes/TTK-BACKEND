from crum import get_current_user
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CoreManager


class AbstractAudit(models.Model):
    """
    An abstract model that manages the modifications made to a model
    """
    is_active = models.BooleanField(
        _('estado'),
        default=True,
        help_text=_(
            'estado'
        ),
        db_column='estado'
    )
    creation_date = models.DateTimeField(
        _('fecha registro'),
        auto_now_add=True,
        help_text=_('fecha registro'),
        db_column='fec_reg'
    )
    created_by = models.CharField(
        _('usuario registrado'),
        max_length=100,  # max length of User.username
        help_text=_('usuario registrado'),
        db_column='usu_reg'
    )
    update_date = models.DateTimeField(
        _('fecha edicion'),
        auto_now=True,
        help_text=_('fecha edicion'),
        db_column='fec_edicion'
    )
    update_by = models.CharField(
        _('usuario edicion'),
        max_length=100,  # max length of User.username
        help_text=_('usuario edicion'),
        db_column='usu_edicion'
    )
    # created_by_user_fullname = models.CharField(
    #     _('user fullname created'),
    #     null=True,
    #     max_length=100,  # max length of User.username
    #     help_text=_('user fullname that created the record')
    # )

    objects = CoreManager()

    class Meta:
        abstract = True

    def get_current_username(self):
        """
        gets the user who logs in or returns the user system
        :return: username
        """
        user = get_current_user()
        if user and user.is_authenticated:
            return getattr(user, user.name, 'system')
        return 'system'

    def on_pre_create(self):
        pass

    def on_pre_save(self):
        pass

    def on_post_create(self):
        pass

    def on_post_save(self):
        pass

    def set_created_by_user_fullname(self):
        if self.pk is None:
            user = get_current_user()
            if user:
                self.created_by_user_fullname = (user.first_name or '') + ' ' + (user.last_name or '')

    def set_created_by(self):
        if self.pk is None:
            self.created_by = self.get_current_username()

    def set_update_by(self):
        self.update_by = self.get_current_username()

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)

    def on_clean(self):
        pass

    def save(self, *args, **kwargs):
        pk = self.pk
        if pk is None:
            self.on_pre_create()
        self.on_pre_save()
        self.set_created_by()
        self.set_update_by()
        self.set_created_by_user_fullname()
        self.on_clean()

        super(AbstractAudit, self).save(*args, **kwargs)
        if pk is None:
            self.on_post_create()
        _skip_post_save = getattr(self, '_skip_post_save', False)
        if not _skip_post_save:
            self.on_post_save()

    def multi_set(self, **kwargs):
        for (key, value) in kwargs.items():
            try:
                setattr(self, key, value)
            except TypeError:
                if type(value) == list:
                    field = getattr(self, key)
                    field.set(value)
        return self

    def multi_save(self, **kwargs):
        self.multi_set(**kwargs)
        self.save()


class AbstractChoice(AbstractAudit):
    """
    An abstract model for and id and name entry (i.e. field).
    """
    name = models.CharField(
        _('nombre'),
        max_length=100,
        help_text=_("Nombre"),
        db_column='nombre'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class AbstractAttachment(AbstractAudit):
    title = models.CharField(max_length=90, null=True, blank=True)
    category = models.CharField(max_length=90, null=True, blank=True)
    description = models.CharField(max_length=90, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} - {}".format(self.id, self.title)
