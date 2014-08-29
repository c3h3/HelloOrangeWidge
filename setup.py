
from setuptools import setup, find_packages

PACKAGES = find_packages(
    exclude = ('*.tests', '*.tests.*', 'tests.*', 'tests'),
)

PACKAGE_DATA = {
    '': ["*.svg"]
}

setup(name="Demo",
      packages=PACKAGES,
      package_data = PACKAGE_DATA,
      # Declare orangedemo package to contain widgets for the "Demo" category
      entry_points={"orange.widgets": ("Demo = orangedemo")},
      )


