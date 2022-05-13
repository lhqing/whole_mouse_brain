import pandas as pd
from ..files import *


class GenomeRef:
    def __init__(self):
        self.ENCODE_BLACKLIST_PATH = ENCODE_BLACKLIST_PATH
        self.GENCODE_MM10_vm22 = GENCODE_MM10_vm22

    def get_gene_metadata(self):
        gene_meta = pd.read_csv(self.GENCODE_MM10_vm22, sep='\t', index_col='gene_id')
        return gene_meta


mm10 = GenomeRef()
