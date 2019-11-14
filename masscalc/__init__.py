"""
massCalc
This is a module that will take a protein sequence and a labeling method and calculate the proteins moelcular weight.
"""

# Add imports here
from .masscalc import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
