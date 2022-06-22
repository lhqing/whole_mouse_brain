from ._cemba import *
from ._aibs import *
from ._broad import *
from ._brain_region import *
from ._ref import *
import pathlib


class AutoPathMixIn:
    def check_file_path_attrs(self):
        for attr in dir(self):
            if not attr.startswith('__') and attr.endswith('_PATH'):
                cur_path = self.__getattribute__(attr)
                found = False
                if pathlib.Path(cur_path).exists():
                    found = True
                else:
                    # try GCP path
                    # change everything before BICCN
                    new_path = cur_path.replace('/gale/netapp/cemba3c', '/mnt/home')
                    if pathlib.Path(new_path).exists():
                        cur_path = new_path
                        found = True

                if found:
                    self.__setattr__(attr, cur_path)
                else:
                    print(f'{attr} do not exist: {cur_path}')
