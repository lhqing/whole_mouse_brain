import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# CEMBA RS1.1
# =================================

# the code to prepare cemba metadata is in
# /home/hanliu/project/cemba/study/BasicFilteringAndPrepareMetadata
CEMBA_SNMC_MAPPING_METRIC = PACKAGE_DIR / 'files/CEMBA.CellMetadata.snmC-seq.small.csv.gz'
CEMBA_SNM3C_MAPPING_METRIC = PACKAGE_DIR / 'files/CEMBA.CellMetadata.snm3C-seq.small.csv.gz'
CEMBA_SNMC_MAPPING_METRIC_FULL_CEMBA = '/home/hanliu/project/cemba/metainfo/CEMBA.CellMetadata.snmC-seq.hdf'
CEMBA_SNM3C_MAPPING_METRIC_FULL_CEMBA = '/home/hanliu/project/cemba/metainfo/CEMBA.CellMetadata.snm3C-seq.hdf'

# the code to prepare cemba file path is in
# /home/hanliu/cemba3c/BICCN/wmb/file_path
CEMBA_SNMC_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.ALLCPaths.csv.gz'
CEMBA_SNM3C_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.ALLCPaths.csv.gz'
CEMBA_SNMC_MCG_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.mCGALLCPaths.csv.gz'
CEMBA_SNM3C_MCG_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.mCGALLCPaths.csv.gz'
