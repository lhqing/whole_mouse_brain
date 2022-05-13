import pandas as pd

from wmb.files import *
from ..annot import BROADTENXCellAnnotation


class BROAD:
    def __init__(self):
        self.BROAD_TENX_SAMPLE_METADATA_PATH = BROAD_TENX_SAMPLE_METADATA_PATH
        self.BROAD_TENX_ZARR_PATH = BROAD_TENX_ZARR_PATH
        self.BROAD_TENX_OUTLIER_IDS_PATH = BROAD_TENX_OUTLIER_IDS_PATH
        self.BROAD_TENX_CELL_TYPE_ANNOTATION_PATH = BROAD_TENX_CELL_TYPE_ANNOTATION_PATH
        return

    def get_tenx_sample_metadata(self):
        df = pd.read_csv(self.BROAD_TENX_SAMPLE_METADATA_PATH, index_col=0)
        df.index.name = 'sample'
        return df

    def get_tenx_outlier_ids(self):
        ids = pd.read_csv(self.BROAD_TENX_OUTLIER_IDS_PATH, index_col=0, header=None).index
        ids.name = 'cell'
        return ids

    def get_tenx_annot(self):
        return BROADTENXCellAnnotation(self.BROAD_TENX_CELL_TYPE_ANNOTATION_PATH,
                                       self.get_tenx_sample_metadata())


broad = BROAD()
