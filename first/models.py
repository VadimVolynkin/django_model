import uuid
import datetime
from enum import Enum

from django.urls import reverse
from django.utils import timezone

from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manufacturer_detail', kwargs={'id': self.pk})


class Car(models.Model):
    name = models.CharField(max_length=200)
    xxx = ['Audi', 'BMW']
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars_related')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'id': self.pk})












    # auto_field = models.AutoField(primary_key=True)
    # small_auto_field = models.SmallAutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    # uuid_field = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # NUMBER TYPES ===========================================================
    # small_integer_field = models.SmallIntegerField(blank=True, null=True)
    # integer_field = models.IntegerField(blank=True, null=True)
    # big_integer_field = models.BigIntegerField(blank=True, null=True)
    # positive_integer_field = models.PositiveIntegerField(blank=True, null=True)
    # positive_small_integer_field = models.PositiveSmallIntegerField(blank=True, null=True)
    # positive_big_integer_field = models.PositiveBigIntegerField(blank=True, null=True)     # not in 3.0 documentation
    # decimal_field = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # float_field = models.FloatField(blank=True, null=True)

    # STRING TYPES ===========================================================
    # char_field = models.CharField(max_length=200, blank=True)
    # text_field = models.TextField(blank=True)
    # slug_field = models.SlugField(max_length=200, blank=True)
    # email_field = models.EmailField(max_length=200, blank=True)
    # url_field = models.URLField(max_length=200, blank=True)
    # generic_ip_address_field = models.GenericIPAddressField(blank=True, null=True)
    # file_path_field = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY, blank=True)

    # DATE and TIME TYPES ====================================================
    # date_field = models.DateField(auto_now_add=True)
    # time_field = models.TimeField(auto_now=True)
    # date_time_field = models.DateTimeField(default=timezone.now())
    # duration_field = models.DurationField()

    # LOGIC TYPES ============================================================
    # boolean_filed = models.BooleanField(default=True)
    # null_boolean_field = models.NullBooleanField(default=False)

    # FILE TYPES =============================================================
    # file_field = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # image_field = models.ImageField(upload_to='image/%Y/%m/%d/', height_field=None, width_field=None)
    # binary_field = models.BinaryField(default=bytes('hello world', 'utf-8'))   # convert string hello world in bytes

    # OTHER TYPES ============================================================
    # integer_choices = models.IntegerChoices('Color', names='RED GREEN BLUE')
    # text_choices = models.TextChoices('Color', names='RED GREEN BLUE')
    # choices = models.Choices('Color', names='RED GREEN BLUE')
    # empty_field = models.Empty()
    # json_field = models.JSONField()



    # NOT in Documentation 3.0
    # integer_choices = models.IntegerChoices()
    # text_choices = models.TextChoices()
    # comma_separated_integer_field = models.CommaSeparatedIntegerField()
    # choices = models.Choices('Color', names='RED GREEN BLUE')
    # ip_address_field = models.IPAddressField()
    # json_field = models.JSONField()