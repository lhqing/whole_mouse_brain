import pandas as pd
from ..files import *


class GenomeRef:
    def __init__(self):
        self.ENCODE_BLACKLIST_PATH = ENCODE_BLACKLIST_PATH
        self.GENCODE_MM10_vm22 = GENCODE_MM10_vm22
        self._gene_id_to_name = None
        self._gene_name_to_id = None


    def get_gene_metadata(self, annot_version='GENCODE_vm22'):
        if annot_version == 'GENCODE_vm22':
            gene_meta = pd.read_csv(self.GENCODE_MM10_vm22, sep='\t', index_col='gene_id')
        else:
            raise NotImplementedError
        return gene_meta

    def _get_gene_id_name_dict(self, annot_version='GENCODE_vm22'):
        if annot_version == 'GENCODE_vm22':
            self._gene_id_to_name = mm10.get_gene_metadata()['gene_name'].to_dict()
            self._gene_name_to_id = {v: k for k, v in self._gene_id_to_name.items()}
        else:
            raise NotImplementedError

    def gene_id_to_name(self, gene_id, annot_version='GENCODE_vm22'):
        if self._gene_id_to_name is None:
            self._get_gene_id_name_dict(annot_version)
        return self._gene_id_to_name[gene_id]

    def gene_name_to_id(self, gene_name, annot_version='GENCODE_vm22'):
        if self._gene_id_to_name is None:
            self._get_gene_id_name_dict(annot_version)
        return self._gene_name_to_id[gene_name]


mm10 = GenomeRef()
