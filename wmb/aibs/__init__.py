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
        self.AIBS_SMART_OUTLIER_IDS_PATH = AIBS_SMART_OUTLIER_IDS_PATH

        self.AIBS_TENX_SAMPLE_METADATA_PATH = AIBS_TENX_SAMPLE_METADATA_PATH
        self.AIBS_TENX_SAMPLE_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_FULL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH
        self.AIBS_TENX_ZARR_PATH = AIBS_TENX_ZARR_PATH
        self.AIBS_TENX_OUTLIER_IDS_PATH = AIBS_TENX_OUTLIER_IDS_PATH
        return

    def get_smart_cell_metadata(self, pass_basic_qc_only=True, remove_outlier_ids=True):
        df = pd.read_csv(self.AIBS_SMART_CELL_METADATA_PATH, index_col=0)
        df.index.name = 'cell'
        if pass_basic_qc_only:
            df = df[df['PassBasicQC']].copy()
        if remove_outlier_ids:
            df = df.drop(self.get_smart_outlier_ids())
        return df

    def get_tenx_sample_metadata(self):
        df = pd.read_csv(self.AIBS_TENX_SAMPLE_METADATA_PATH, index_col=0)
        
        # three sample has missing values in the current manifest file, 05/08/2022
        df.fillna('nan', inplace=True)

        df.index.name = 'sample'
        return df

    def get_tenx_outlier_ids(self):
        ids = pd.read_csv(self.AIBS_TENX_OUTLIER_IDS_PATH, index_col=0, header=None).index
        ids.name = 'cell'
        return ids

    def get_smart_outlier_ids(self):
        ids = pd.read_csv(self.AIBS_SMART_OUTLIER_IDS_PATH, index_col=0, header=None).index
        ids.name = 'cell'
        return ids


aibs = AIBS()
