from django.db import models


class CoreManager(models.Manager):
    def actives(self):
        return super(CoreManager, self).get_queryset().filter(estado=True)


class LogisticaManager(models.Manager):

    def get_queryset(self):
        return super(LogisticaManager, self).get_queryset().using('logistica')
