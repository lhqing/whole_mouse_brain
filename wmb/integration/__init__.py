from ..annot.integration import IntegrationResultZarr
from ..files._integration import *


class BICCNIntegration:
    def __init__(self):
        self.MC_M3C_INTEGRATION_ZARR = MC_M3C_INTEGRATION_ZARR
        self.MC_ATAC_INTEGRATION_ZARR = MC_ATAC_INTEGRATION_ZARR
        self.MC_SMART_INTEGRATION_ZARR = MC_SMART_INTEGRATION_ZARR
        self.MC_AIBS_TENX_INTEGRATION_ZARR = MC_AIBS_TENX_INTEGRATION_ZARR
        self.MC_BROAD_TENX_INTEGRATION_ZARR = MC_BROAD_TENX_INTEGRATION_ZARR
        self.MC_L4_MULTIOME_ZARR = MC_L4_MULTIOME_ZARR
        return

    def get_mc_m3c_integration(self):
        return IntegrationResultZarr(self.MC_M3C_INTEGRATION_ZARR)

    def get_mc_atac_integration(self):
        return IntegrationResultZarr(self.MC_ATAC_INTEGRATION_ZARR)

    def get_mc_smart_integration(self):
        return IntegrationResultZarr(self.MC_SMART_INTEGRATION_ZARR)

    def get_mc_aibs_tenx_integration(self):
        return IntegrationResultZarr(self.MC_AIBS_TENX_INTEGRATION_ZARR)

    def get_mc_broad_tenx_integration(self):
        return IntegrationResultZarr(self.MC_BROAD_TENX_INTEGRATION_ZARR)


biccn_integration = BICCNIntegration()
