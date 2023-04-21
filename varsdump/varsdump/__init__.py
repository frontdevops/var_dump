# import sys
# if sys.version_info < (3, 10, 8):
#     raise ImportError('Your Python version {0} is not supported by MagicConfig, please install '
#                       'Python 3.10.8+'.format('.'.join(map(str, sys.version_info[:3]))))

from .lib import varsdump

__all__ = (
    "varsdump"
)

__version__ = '1.0.0'

