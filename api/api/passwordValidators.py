from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class ComplexPasswordValidator:
    """
    Validate whether the password contains minimum one uppercase, one digit and one symbol.
    """
    def validate(self, password, user=None):
        if re.search('[^A-Za-z0-9]', password)==None:
            raise ValidationError(
                _("Your password must contain at least one special character ."),
                code='password_is_weak',
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 number, 1 uppercase and 1 non-alphanumeric character.")