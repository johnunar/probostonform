from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from idvalidator.ares import validate_business_id_checksum, validate_business_id_ares


def validate_business_id(business_id):
    if not validate_business_id_checksum(business_id):
        raise ValidationError(
            _('%(value)s is not a valid business id'),
            params={'value': business_id},
        )

    if not validate_business_id_ares(business_id):
        raise ValidationError(
            _('%(value)s was not found in the ARES database'),
            params={'value': business_id},
        )
