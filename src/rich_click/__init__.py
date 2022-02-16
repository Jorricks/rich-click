"""
rich-click is a minimal Python module to combine the efforts
of the excellent packages 'rich' and 'click'.

The intention is to provide attractive help output from
click, formatted with rich, with minimal customisation required.
"""

__version__ = "0.4.0.dev0"

from click import *
from .rich_click import rich_format_help
from .rich_click import rich_format_error
from .rich_click import Group
from .rich_click import Command
