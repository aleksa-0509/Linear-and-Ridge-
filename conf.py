Original file is located at
    https://colab.research.google.com/drive/1CiinNpAk6ydLkZbQIFJ30U-zcFopjAnh

pip install dynaconf

import logging
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['conf\\settings.toml'],
)

logging.basicConfig(level=settings.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
