"""
Notes:
    1. 3 10X samples has h5 missing manifest,
    2. 131 10X sample has manifest, missing h5. see AIBS_tenx_missing_info.txt
    3. SMART-seq data all has manifest
    4. 9895 SMART-seq cell has manifest, no data. see AIBS_SMART_missing_info.txt
    5. Need to clean up AIBS regions, get colors, standardize
    6. Current 10X sample metadata
        816: shared by Zizhen Yao
        688: files having h5 on Terra, but only 685 has metadata
"""

import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# AIBS SMART
# =================================

AIBS_SMART_CELL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.SMART.KeyCellMetadata.213261.csv.gz'
AIBS_SMART_CELL_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.SMART.CellMetadata.213261.csv.gz'
# TODO, zarr need to be sorted after basic clustering
AIBS_SMART_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/AIBS_SMART/AIBS.SMART.ordered.zarr'

# gene metadata
# clustering, outlier

# =================================
# AIBS 10X v2 and v3
# =================================

AIBS_TENX_SAMPLE_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.KeySampleMetadata.688.csv.gz'
AIBS_TENX_SAMPLE_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.SampleMetadata.688.csv.gz'
AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.KeySampleMetadata.816.csv.gz'
AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.SampleMetadata.816.csv.gz'
# TODO, zarr need to be sorted after basic clustering
AIBS_TENX_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/AIBS_TENX/AIBS.10X.unordered.zarr'
