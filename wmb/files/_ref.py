import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

ENCODE_BLACKLIST_PATH = PACKAGE_DIR / "files/mm10-blacklist.v2.bed.gz"

