# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
# python setup.py sdist
# twine upload dist/*

from distutils.core import setup

with open("README.md", "r") as readme:
  long_description = readme.read()

setup(
  name = 'magforce',
  packages = ['magforce'],
  version = '2.2',
  license='agpl-3.0',
  description = 'Free Python3 library for easy calculation and plotting of magnetic forces',
  long_description=long_description,
  author = 'Mateus Rodolfo',
  author_email = 'mateusgrodolfo@gmail.com',
  url = 'https://github.com/MateusRodolfo/magforce',
  download_url = 'https://github.com/MateusRodolfo/magforce/archive/v2.2.tar.gz',
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
    'LICENSE :: OSI APPROVED :: GNU AFFERO GENERAL PUBLIC LICENSE V3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)