# for PIPy publishing
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
# python setup.py sdist
# twine upload dist/*

from distutils.core import setup

long_description = 'Free Python3 library for easy calculation and plotting of magnetic forces.\n\n' \
                   'Made by Mateus Rodolfo during an internship at LNCMI (CNRS) supervised by Eric Beaugnon.\n\n' \
                   'Uses the magpylib python library. Thank you Mr Michael Ortner for all the help provided with magpylib.'


setup(
  name = 'magforce',
  packages = ['magforce'],
  version = '3.4',
  license = 'agpl-3.0',
  description = 'Free Python3 library for easy calculation and plotting of magnetic forces',
  long_description = long_description,
  author = 'Mateus Rodolfo',
  author_email = 'mateusgrodolfo@gmail.com',
  url = 'https://github.com/MateusRodolfo/magforce',
  download_url = 'https://github.com/MateusRodolfo/magforce/archive/refs/tags/3.4.tar.gz',
  keywords = ['python', 'python3', 'magnet'],
  install_requires=[
          'matplotlib<3.4',
          'numpy<1.20',
          'magpylib==2.3.0-beta',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'Natural Language :: English',
    'Topic :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Physics',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

