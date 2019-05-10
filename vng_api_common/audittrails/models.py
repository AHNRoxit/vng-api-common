import uuid

from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..descriptors import GegevensGroepType
from ..constants import CommonResourceAction


class AuditTrail(models.Model):
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4,
        help_text="Unieke resource identifier (UUID4)"
    )
    bron = models.CharField(max_length=50)
    actie = models.CharField(max_length=50)
    actieWeergave = models.CharField(
        max_length=200,
        blank=True
    )
    resultaat = models.IntegerField()
    hoofdObject = models.URLField(max_length=1000)
    resource = models.CharField(max_length=50)
    resourceUrl = models.URLField(max_length=1000)
    aanmaakdatum = models.DateTimeField(auto_now=True)

    oud = JSONField(null=True, encoder=DjangoJSONEncoder)
    nieuw = JSONField(null=True, encoder=DjangoJSONEncoder)
    wijzigingen = GegevensGroepType({
        'oud': oud,
        'nieuw': nieuw,
    })
