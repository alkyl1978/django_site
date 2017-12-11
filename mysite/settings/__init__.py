try:
    from mysite.settings.local import *
except ImportError:
    from mysite.settings.common import *

