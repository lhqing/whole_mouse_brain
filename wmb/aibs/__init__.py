import pandas as pd

from wmb.files import *


def _get_mapping_metric(path, pass_basic_qc_only=True):
    df = pd.read_csv(path, index_col=0)
    df.index.name = 'cell'
    if pass_basic_qc_only:
        df = df[df['PassBasicQC']].copy()
    return df


class AIBS:
    def __init__(self):
        self.AIBS_SMART_CELL_METADATA_PATH = AIBS_SMART_CELL_METADATA_PATH
        self.AIBS_SMART_CELL_FULL_METADATA_PATH = AIBS_SMART_CELL_FULL_METADATA_PATH
        self.AIBS_SMART_ZARR_PATH = AIBS_SMART_ZARR_PATH
        self.AIBS_TENX_SAMPLE_METADATA_PATH = AIBS_TENX_SAMPLE_METADATA_PATH
        self.AIBS_TENX_SAMPLE_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_FULL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH
        self.AIBS_TENX_ZARR_PATH = AIBS_TENX_ZARR_PATH
        return

    def get_smart_cell_metadata(self, pass_basic_qc_only=True):
        df = pd.read_csv(self.AIBS_SMART_CELL_METADATA_PATH, index_col=0)
        df.index.name = 'cell'
        if pass_basic_qc_only:
            df = df[df['PassBasicQC']].copy()
        return df

    def get_tenx_sample_metadata(self):
        df = pd.read_csv(self.AIBS_TENX_SAMPLE_METADATA_PATH, index_col=0)
        df.index.name = 'sample'
        return df


aibs = AIBS()
