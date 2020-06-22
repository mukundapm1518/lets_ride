from django.db import models
from django.core.exceptions import ValidationError
from lets_ride.models.user import User
from lets_ride.models.share_ride import ShareRide
from lets_ride.constants.enums import AssetSensitivity
from lets_ride.constants.constants \
    import ASSETTYPE, ASSET_SENSITIVITY, STATUS


def validate_asset_quantity(value):
    if value <= 0:
        raise ValidationError("asset_quantity cann't be negative")

def validate_asset_type(value):
    if value not in ASSETTYPE:
        raise ValidationError("Asset type is not in ",ASSETTYPE)


def validate_asset_sensitivity(value):
    if value not in ASSET_SENSITIVITY:
        raise ValidationError("AssetSensitivity not in ",ASSET_SENSITIVITY)


class AssetRequest(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)
    asset_quantity = models.IntegerField(validators=[validate_asset_quantity])
    asset_type_others = models.CharField(max_length=100, null=True, blank=True)
    deliver_to = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    asset_type = models.CharField(
        choices=ASSETTYPE,
        max_length=50,
        validators=[validate_asset_type]
    )

    asset_sensitivity = models.CharField(
        choices=ASSET_SENSITIVITY,
        max_length=50,
        validators=[validate_asset_sensitivity]
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'asset_requests'
    )

    accepted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assets_accepted",
        null=True,
        blank=True
    )


    def save(self, *args, **kwargs):

        if self.flexible_timings and self.travel_date_time:
            raise ValidationError(
                """
                you cannot select flexible
                timings and travel datetime at same time
                """
            )
        if self.flexible_timings is False:
            if self.flexible_from_date_time or self.flexible_to_date_time:
                raise ValidationError(
                    """
                    you cannot select datetime range
                    when flexible timings set to False
                    """
                )
        super().save(*args, **kwargs)

