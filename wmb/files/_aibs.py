"""
Notes:
    1. some 10X samples missing h5 or manifest, see AIBS_missing_info.txt 685
    2. Need to clean up AIBS regions, get colors, standardize

"""

import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# AIBS SMART
# =================================

AIBS_SMART_CELL_METADATA_PATH = ''
AIBS_SMART_CELL_FULL_METADATA_PATH = ''
AIBS_SMART_ZARR_PATH = ''

# gene metadata
# clustering, outlier

# =================================
# AIBS 10X v2 and v3
# =================================

AIBS_TENX_SAMPLE_METADATA_PATH = ''
AIBS_TENX_SAMPLE_FULL_METADATA_PATH = ''
AIBS_TENX_ZARR_PATH = ''


