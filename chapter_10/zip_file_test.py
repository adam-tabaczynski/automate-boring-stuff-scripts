import zipfile, os
from pathlib import Path

p = Path.home()
example_zip = zipfile.ZipFile(p / 'hello.zip')
example_zip.namelist()