from .annot import CellAnnotation
from ..aibs import aibs
from ..brain_region import brain
from ..files import \
    AIBS_TENX_CELL_TYPE_ANNOTATION_PATH, \
    AIBS_SMART_CELL_TYPE_ANNOTATION_PATH


class AIBSTENXCellAnnotation(CellAnnotation):
    def __init__(self, annot_path=AIBS_TENX_CELL_TYPE_ANNOTATION_PATH):
        super().__init__(annot_path)

        # add AIBS specific attributes
        self.annot['sample'] = self.annot.get_index('cell').map(lambda i: i.split('-')[0])
        sample_meta = aibs.get_tenx_sample_metadata()

        sample_meta['MajorRegion'] = sample_meta['Structure'].map(
            brain.map_dissection_region_to_major_region())
        self.annot['MajorRegion'] = self.annot['sample'].to_pandas().map(sample_meta['MajorRegion'])

        sample_meta['SubRegion'] = sample_meta['Structure'].map(
            brain.map_dissection_region_to_sub_region())
        self.annot['SubRegion'] = self.annot['sample'].to_pandas().map(sample_meta['SubRegion'])
        return


class AIBSSMARTCellAnnotation(CellAnnotation):
    def __init__(self, annot_path=AIBS_SMART_CELL_TYPE_ANNOTATION_PATH):
        super().__init__(annot_path)

        cell_meta = aibs.get_smart_cell_metadata()
        self.annot['MajorRegion'] = cell_meta['Substructure'].map(
            brain.map_dissection_region_to_major_region())

        self.annot['SubRegion'] = cell_meta['Substructure'].map(
            brain.map_dissection_region_to_sub_region())
        return
