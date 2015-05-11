from django.db import models
from cms.models.fields import PlaceholderField
# Create your models here.


class Service(models.Model):
    """
        services of digital works
    """
    name = PlaceholderField('name', related_name='service_name')
    description = PlaceholderField('description',
                                   related_name='service_description')
    icon = PlaceholderField('icon', related_name='service_icon')
    status = models.BooleanField(default=False,
                                 verbose_name=u'Servicio activo')
    order = models.PositiveIntegerField(verbose_name='Orden')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')

    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Servicio'
        verbose_name_plural = u'Servicios'
