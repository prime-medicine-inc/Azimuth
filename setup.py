# from Cython.Build import cythonize
from setuptools import setup


setup(name='Azimuth',
      version='0.1.2',
      author='Nicolo Fusi and Jennifer Listgarten',
      author_email="fusi@microsoft.com, jennl@microsoft.com",
      description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 guide efficiency"),
      packages=["azimuth", "azimuth.features", "azimuth.models", "azimuth.tests"],
      package_data={'azimuth': ['saved_models/*.*', 'data/*.*']},
      install_requires=['scipy', 'numpy>=1.6.1', 'nose', 'scikit-learn', 'pandas', 'biopython', 'xlrd'],
      license="BSD",
      # ext_modules=cythonize("ssk_cython.pyx"),
      )
