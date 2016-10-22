from django.db              import models
from django.core.validators import RegexValidator


class Hospital(models.Model):
    id             = models.CharField(max_length=20, primary_key=True)
    created        = models.DateTimeField(auto_now_add=True)
    name           = models.CharField(max_length=128)
    latitude       = models.FloatField(null=True)
    longitude      = models.FloatField(null=True)
    phone_regex    = RegexValidator(regex=r'\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*',
                                    message="Phone number must be entered in the format:"
                                            " '+999999999'. Up to 15 digits allowed.")
    contact        = models.CharField(validators=[phone_regex], null=True, max_length=15)
    address        = models.CharField(max_length=256, null=True)
    business_hours = models.CharField(max_length=10,  null=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{}'.format(self.name)
