"""A short description of the project (less than one line)."""

# Add imports here
from .functions import *

import textwrap

wrap_text = textwrap.TextWrapper(width=120)
wrap_stdout = textwrap.TextWrapper(width=120)

# Handle versioneer
from ._version import get_versions  # noqa: E402

__author__ = """Jing Chen"""
__email__ = "jchenmol@vt.edu"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions