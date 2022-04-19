import pandas as pd

from wmb.files import *


class CEMBASnmCAndSnm3C:
    def __init__(self):
        return

    @classmethod
    def _get_mapping_metric(cls, path, pass_basic_qc_only=True):
        df = pd.read_csv(path, index_col=0)
        df.index.name = 'cell'
        if pass_basic_qc_only:
            df = df[df['PassBasicQC']].copy()
        return df

    @classmethod
    def get_mc_mapping_metric(cls, pass_basic_qc_only=True):
        df = cls._get_mapping_metric(CEMBA_SNMC_MAPPING_METRIC, pass_basic_qc_only)
        return df

    @classmethod
    def get_m3c_mapping_metric(cls, pass_basic_qc_only=True):
        df = cls._get_mapping_metric(CEMBA_SNM3C_MAPPING_METRIC, pass_basic_qc_only)
        return df

    @classmethod
    def get_mc_m3c_mapping_metric(cls, pass_basic_qc_only=True):
        df1 = cls.get_mc_mapping_metric(pass_basic_qc_only)
        df2 = cls.get_m3c_mapping_metric(pass_basic_qc_only)
        df = pd.concat([df1, df2])
        return df

    @classmethod
    def get_allc_path(cls, dataset, allc_type, store='gale'):
        """
        read ALLC path series for certain dataset and allc_type

        Parameters
        ----------
        dataset
            Can be "mc", "m3c"
        allc_type
            Can be "full", "mcg". The mCG ALLC contains CpG only

        Returns
        -------
        Series of cell-id by ALLC path on GALE
        """
        if store != 'gale':
            raise NotImplementedError('store must be "gale"')

        dataset = dataset.lower()
        allc_type = allc_type.lower()

        def _read_file_paths(p):
            s = pd.read_csv(p, index_col=0, squeeze=True)
            s.index.name = 'cell'
            return s

        if dataset == 'mc' and allc_type == 'full':
            allc_paths = _read_file_paths(CEMBA_SNMC_ALLC_PATH)
        elif dataset == 'm3c' and allc_type == 'full':
            allc_paths = _read_file_paths(CEMBA_SNM3C_ALLC_PATH)
        elif dataset == 'mc' and allc_type == 'mcg':
            allc_paths = _read_file_paths(CEMBA_SNMC_MCG_ALLC_PATH)
        elif dataset == 'mc' and allc_type == 'mcg':
            allc_paths = _read_file_paths(CEMBA_SNM3C_MCG_ALLC_PATH)
        else:
            raise ValueError('Got invalid value for dataset or allc_type. '
                             'Check doc string for allowed values.')
        return allc_paths


# mcds path
# cluster assignments
