import pandas as pd

from wmb.files import *


def _get_mapping_metric(path, pass_basic_qc_only=True):
    df = pd.read_csv(path, index_col=0)
    df.index.name = 'cell'
    if pass_basic_qc_only:
        df = df[df['PassBasicQC']].copy()
    return df


class CEMBASnmCAndSnm3C:
    def __init__(self):
        self.CEMBA_SNMC_MAPPING_METRIC_PATH = CEMBA_SNMC_MAPPING_METRIC_PATH
        self.CEMBA_SNM3C_MAPPING_METRIC_PATH = CEMBA_SNM3C_MAPPING_METRIC_PATH
        self.CEMBA_SNMC_FULL_MAPPING_METRIC_PATH = CEMBA_SNMC_FULL_MAPPING_METRIC_PATH
        self.CEMBA_SNM3C_FULL_MAPPING_METRIC_PATH = CEMBA_SNM3C_FULL_MAPPING_METRIC_PATH
        self.CEMBA_SNMC_ALLC_PATH = CEMBA_SNMC_ALLC_PATH
        self.CEMBA_SNM3C_ALLC_PATH = CEMBA_SNM3C_ALLC_PATH
        self.CEMBA_SNMC_MCG_ALLC_PATH = CEMBA_SNMC_MCG_ALLC_PATH
        self.CEMBA_SNM3C_MCG_ALLC_PATH = CEMBA_SNM3C_MCG_ALLC_PATH
        self.CEMBA_SNM3C_CONTACT_PATH = CEMBA_SNM3C_CONTACT_PATH
        self.CEMBA_SNM3C_10K_RAW_COOL_PATH = CEMBA_SNM3C_10K_RAW_COOL_PATH
        self.CEMBA_SNM3C_25K_RAW_COOL_PATH = CEMBA_SNM3C_25K_RAW_COOL_PATH
        self.CEMBA_SNM3C_100K_RAW_COOL_PATH = CEMBA_SNM3C_100K_RAW_COOL_PATH
        self.CEMBA_SNM3C_10K_IMPUTED_COOL_PATH = CEMBA_SNM3C_10K_IMPUTED_COOL_PATH
        self.CEMBA_SNM3C_25K_IMPUTED_COOL_PATH = CEMBA_SNM3C_25K_IMPUTED_COOL_PATH
        self.CEMBA_SNM3C_100K_IMPUTED_COOL_PATH = CEMBA_SNM3C_100K_IMPUTED_COOL_PATH
        self.CEMBA_SNMC_MCDS_PATH = CEMBA_SNMC_MCDS_PATH
        self.CEMBA_SNM3C_MCDS_PATH = CEMBA_SNM3C_MCDS_PATH
        self.CEMBA_LIU_2021_NATURE_SNMC_METADATA_PATH = CEMBA_LIU_2021_NATURE_SNMC_METADATA_PATH
        return

    def get_mc_mapping_metric(self, pass_basic_qc_only=True):
        df = _get_mapping_metric(self.CEMBA_SNMC_MAPPING_METRIC_PATH, pass_basic_qc_only)
        return df

    def get_m3c_mapping_metric(self, pass_basic_qc_only=True):
        df = _get_mapping_metric(self.CEMBA_SNM3C_MAPPING_METRIC_PATH, pass_basic_qc_only)
        return df

    def get_mc_m3c_mapping_metric(self, pass_basic_qc_only=True):
        df1 = self.get_mc_mapping_metric(pass_basic_qc_only)
        df2 = self.get_m3c_mapping_metric(pass_basic_qc_only)
        df = pd.concat([df1, df2])
        if 'Technology' in df:
            name_map = {i: i for i in df['Technology'].unique()}
            name_map['snmC-seq2'] = 'snmC-seq2&3'
            name_map['snmC-seq3'] = 'snmC-seq2&3'
            df['Technology2'] = df['Technology'].map(name_map)
        return df

    def get_allc_path(self, dataset, allc_type):
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
        dataset = dataset.lower()
        allc_type = allc_type.lower()

        def _read_file_paths(p):
            s = pd.read_csv(p, index_col=0, squeeze=True)
            s.index.name = 'cell'
            return s

        if dataset == 'mc' and allc_type == 'full':
            allc_paths = _read_file_paths(self.CEMBA_SNMC_ALLC_PATH)
        elif dataset == 'm3c' and allc_type == 'full':
            allc_paths = _read_file_paths(self.CEMBA_SNM3C_ALLC_PATH)
        elif dataset == 'mc' and allc_type == 'mcg':
            allc_paths = _read_file_paths(self.CEMBA_SNMC_MCG_ALLC_PATH)
        elif dataset == 'mc' and allc_type == 'mcg':
            allc_paths = _read_file_paths(self.CEMBA_SNM3C_MCG_ALLC_PATH)
        else:
            raise ValueError('Got invalid value for dataset or allc_type. '
                             'Check doc string for allowed values.')
        return allc_paths

    def get_m3c_contact_path(self):
        s = pd.read_csv(self.CEMBA_SNM3C_CONTACT_PATH, index_col=0, squeeze=True)
        s.index.name = 'cell'
        return s

    def get_m3c_cool_path(self, resolution, cool_type='imputed'):
        """
        read ALLC path series for certain dataset and allc_type

        Parameters
        ----------
        resolution
            Can be "10K", "25K", "100K"
        cool_type
            Can be "raw", "imputed". The mCG ALLC contains CpG only

        Returns
        -------
        Series of cell-id by COOL path on GALE
        """
        resolution = resolution.upper()
        cool_type = cool_type.lower()

        def _read_file_paths(p):
            s = pd.read_csv(p, index_col=0, squeeze=True)
            s.index.name = 'cell'
            return s

        if resolution == '10K':
            if cool_type == 'raw':
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_10K_RAW_COOL_PATH)
            else:
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_10K_IMPUTED_COOL_PATH)
        elif resolution == '25K':
            if cool_type == 'raw':
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_25K_RAW_COOL_PATH)
            else:
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_25K_IMPUTED_COOL_PATH)
        elif resolution == '100K':
            if cool_type == 'raw':
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_100K_RAW_COOL_PATH)
            else:
                cool_paths = _read_file_paths(self.CEMBA_SNM3C_100K_IMPUTED_COOL_PATH)
        else:
            raise ValueError('Got invalid value for resolution or cool_type. '
                             'Check doc string for allowed values.')
        return cool_paths

    def get_liu_2021_mc_metadata(self):
        return pd.read_csv(self.CEMBA_LIU_2021_NATURE_SNMC_METADATA_PATH, index_col=0)


cemba = CEMBASnmCAndSnm3C()
