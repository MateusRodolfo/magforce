# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
# python setup.py sdist
# twine upload dist/*

from distutils.core import setup

long_description = 'Free Python3 library for easy calculation and plotting of magnetic forces.\n\n' \
                   'Made by [Mateus Rodolfo](https://www.linkedin.com/in/mateusgrodolfo/) during an internship at LNCMI (CNRS) supervised by Eric Beaugnon.\n\n' \
                   'Uses the [magpylib](https://www.sciencedirect.com/science/article/pii/S2352711020300170) python library.\n\n' \
                   'Thanks [Mr Ortner](https://www.linkedin.com/in/michael-ortner-b6b724143/) for all  the help provided.\n\n' \
                   '[Examples files](https://github.com/MateusRodolfo/magforce/tree/master/examples) using the source code (no imports), using the library as an import as well as magpylib examples for magnet setup.'

setup(
  name = 'magforce',
  packages = ['magforce'],
  version = '2.4',
  license='agpl-3.0',
  description = 'Free Python3 library for easy calculation and plotting of magnetic forces',
  long_description=long_description,
  author = 'Mateus Rodolfo',
  author_email = 'mateusgrodolfo@gmail.com',
  url = 'https://github.com/MateusRodolfo/magforce',
  download_url = 'https://github.com/MateusRodolfo/magforce/archive/v2.4.tar.gz',
  keywords = ['python', 'python3', 'magnet'],
  install_requires=[
          'magpylib',
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)