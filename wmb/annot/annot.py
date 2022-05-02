import xarray as xr


class CellAnnotation(xr.Dataset):
    __slots__ = ()

    def __init__(self, annot_path):
        annot = xr.open_zarr(annot_path)
        super().__init__(data_vars=annot.data_vars, coords=annot.coords, attrs=annot.attrs)

        # determine cluster hierarchy list
        cluster_data_var = [] 
        for var_name in self.attrs['cluster_hierarchy']:
            cluster_data_var += var_name
        self.attrs['cluster_data_var'] = cluster_data_var

        # fill cluster cat if the annotation exists
        for var_name in cluster_data_var:
            if f'{var_name}_cat' in self.attrs:
                self[var_name] = self[var_name].to_pandas().map(
                    {i: c for i, c in enumerate(self.attrs[f'{var_name}_cat'])})
        self._concat_hierarchy_label()
        return

    def _concat_hierarchy_label(self):
        """Concatenate hierarchy labels to make lower level labels unique"""
        for hierarchy_list in self.cluster_hiearchy:
            for i, var_name in enumerate(hierarchy_list):
                if i > 0:
                    self[var_name] = self[hierarchy_list[i - 1]] + \
                                     '_' + self[var_name]
        return
