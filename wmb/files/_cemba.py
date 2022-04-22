import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# CEMBA RS1.1
# =================================

# the code to prepare cemba metadata is in
# /home/hanliu/project/cemba/study/BasicFilteringAndPrepareMetadata 04/20/2022
CEMBA_SNMC_MAPPING_METRIC_PATH = PACKAGE_DIR / 'files/CEMBA.CellMetadata.snmC-seq.small.csv.gz'
CEMBA_SNM3C_MAPPING_METRIC_PATH = PACKAGE_DIR / 'files/CEMBA.CellMetadata.snm3C-seq.small.csv.gz'
CEMBA_SNMC_FULL_MAPPING_METRIC_PATH = '/home/hanliu/project/cemba/metainfo/CEMBA.CellMetadata.snmC-seq.hdf'
CEMBA_SNM3C_FULL_MAPPING_METRIC_PATH = '/home/hanliu/project/cemba/metainfo/CEMBA.CellMetadata.snm3C-seq.hdf'

# the code to prepare cemba file path is in
# /home/hanliu/cemba3c/BICCN/wmb/file_path 04/20/2022
CEMBA_SNMC_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.ALLCPaths.csv.gz'
CEMBA_SNM3C_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.ALLCPaths.csv.gz'
CEMBA_SNMC_MCG_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.mCGALLCPaths.csv.gz'
CEMBA_SNM3C_MCG_ALLC_PATH = PACKAGE_DIR / 'files/CEMBA.snmC.mCGALLCPaths.csv.gz'

# snm3C contact related
# /home/hanliu/cemba3c/BICCN/wmb/file_path 04/20/2022
CEMBA_SNM3C_CONTACT_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.ContactPaths.csv.gz'
CEMBA_SNM3C_10K_RAW_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.10KRawCoolURLs.csv.gz'
CEMBA_SNM3C_25K_RAW_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.25KRawCoolURLs.csv.gz'
CEMBA_SNM3C_100K_RAW_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.100KRawCoolURLs.csv.gz'
CEMBA_SNM3C_10K_IMPUTED_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.10KImputedCoolURLs.csv.gz'
CEMBA_SNM3C_25K_IMPUTED_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.25KImputedCoolURLs.csv.gz'
CEMBA_SNM3C_100K_IMPUTED_COOL_PATH = PACKAGE_DIR / 'files/CEMBA.snm3C.100KImputedCoolURLs.csv.gz'

# MCDS Path 04/20/2022
CEMBA_SNMC_MCDS_PATH = '/gale/netapp/cemba3c/BICCN/CEMBA_RS1/dataset/CEMBA.snmC.mcds'
CEMBA_SNM3C_MCDS_PATH = '/gale/netapp/cemba3c/BICCN/CEMBA_3C/mcds/CEMBA.snm3C.mcds'
# separate MCDS subject to delete
# CEMBA_SNM3C_MCDS_PATH = '/gale/netapp/cemba3c/BICCN/CEMBA_3C/mcds/mcds/*.mcds'
# TODO one last region need to generate, then complete the ensemble clustering

# snm3C compartment, embedding, domain
CEMBA_SNM3C_3C_ZARR = None

# cluster assignments
# TODO first round clustering, mark clustering based outliers
# TODO second round clustering, finalize cluster labels

# Liu 2021 Nature metadata
# cell class, major type, subtype
# outliers
# colors
CEMBA_LIU_2021_NATURE_SNMC_METADATA_PATH = PACKAGE_DIR / 'files/CEMBA.Liu2021Nature.snmC.metadata.csv.gz'

# Brain region metadata

