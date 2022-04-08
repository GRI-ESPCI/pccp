import os
from collections import OrderedDict
from flask import Markup

# Role levels

ADMIN = 0
EDITOR = 1
USER_ROLE = {
    ADMIN: 'Administrateur',
    EDITOR: 'Éditeur'
}
USER_ROLE = OrderedDict(sorted(USER_ROLE.items()))
