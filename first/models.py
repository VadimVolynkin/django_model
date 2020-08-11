import uuid

from django.db import models
from django.conf import settings

class SmallAutoFieldClass(models.Model):
    # auto_field = models.AutoField(primary_key=True)
    small_auto_field = models.SmallAutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    # uuid_field = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # NUMBERS TYPE ===========================================================
    # small_integer_field = models.SmallIntegerField(blank=True, null=True)
    # integer_field = models.IntegerField(blank=True, null=True)
    # big_integer_field = models.BigIntegerField(blank=True, null=True)
    # positive_integer_field = models.PositiveIntegerField(blank=True, null=True)
    # positive_small_integer_field = models.PositiveSmallIntegerField(blank=True, null=True)
    # positive_big_integer_field = models.PositiveBigIntegerField(blank=True, null=True)     # not in 3.0 documentation
    # decimal_field = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # float_field = models.FloatField(blank=True, null=True)

    # STRINGS TYPE ===========================================================
    char_field = models.CharField(max_length=200, blank=True)
    text_field = models.TextField(blank=True)
    slug_field = models.SlugField(max_length=200, blank=True)
    email_field = models.EmailField(max_length=200, blank=True)
    url_field = models.URLField(max_length=200, blank=True)
    generic_ip_address_field = models.GenericIPAddressField(blank=True, null=True)
    file_path_field = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY, blank=True)










    # НЕТ В ДОКУМЕНТАЦИИ 3.0
    # choices = models.Choices()
    # integer_choices = models.IntegerChoices()
    # text_choices = models.TextChoices()
    # comma_separated_integer_field = models.CommaSeparatedIntegerField()
    # empty_field = models.Empty()
    # ip_adress_field = models.IPAddressField()
    # json_field = models.JSONField()