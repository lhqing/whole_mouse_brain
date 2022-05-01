import xarray as xr


class CellAnnotation:
    def __init__(self, annot_path):
        self.annot = xr.open_zarr(annot_path)

        # determine cluster hierarchy list
        self.cluster_hierarchy = self.annot.attrs['cluster_hierarchy']
        self.cluster_data_var = []
        for var_name in self.cluster_hierarchy:
            self.cluster_data_var += var_name

        # determine coordinate variables
        self.coord_data_var = []
        for k, v in self.annot.attrs.items():
            if k.endswith('_coord'):
                self.coord_data_var += v

        # fill cluster cat if the annotation exists
        for var_name in self.cluster_data_var:
            if f'{var_name}_cat' in self.annot.attrs:
                self.annot[var_name] = self.annot[var_name].to_pandas().map(
                    {i: c for i, c in enumerate(self.annot.attrs[f'{var_name}_cat'])})
        self._concat_hierarchy_label()
        return

    def _concat_hierarchy_label(self):
        """Concatenate hierarchy labels to make lower level labels unique"""
        for hierarchy_list in self.cluster_hierarchy:
            for i, var_name in hierarchy_list:
                if i > 0:
                    self.annot[var_name] = self.annot[hierarchy_list[i - 1]] + \
                                           '_' + self.annot[var_name]
        return
