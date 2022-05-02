from .annot import CellAnnotation

from .. import broad
from ..brain_region import brain
from ..files import BROAD_TENX_CELL_TYPE_ANNOTATION_PATH


class BROADTENXCellAnnotation(CellAnnotation):
    __slots__ = ()

    def __init__(self, annot_path=BROAD_TENX_CELL_TYPE_ANNOTATION_PATH):
        super().__init__(annot_path)

        # add BROAD specific attributes
        self['sample'] = self.get_index('cell').map(lambda i: i[:-18])
        sample_meta = broad.get_tenx_sample_metadata()

        sample_meta['MajorRegion'] = sample_meta['DissectionRegion'].map(
            brain.map_dissection_region_to_major_region())
        self['MajorRegion'] = self['sample'].to_pandas().map(sample_meta['MajorRegion'])

        sample_meta['SubRegion'] = sample_meta['DissectionRegion'].map(
            brain.map_dissection_region_to_sub_region())
        self['SubRegion'] = self['sample'].to_pandas().map(sample_meta['SubRegion'])
        return
