from distutils.core import setup
setup(
  name = 'magforce',         # How you named your package folder (MyLib)
  packages = ['magforce'],   # Chose the same as "name"
  version = '1.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'free python3 library for easy calculation and plotting of magnetic forces',   # Give a short description about your library
  author = 'Mateus Rodolfo',                   # Type in your name
  author_email = 'mateusgrodolfo@gmail.com',      # Type in your E-Mail
  url = 'https://www.linkedin.com/in/mateusgrodolfo/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/MateusRodolfo/magforce/archive/v1.7-beta.tar.gz',    # I explain this later on
  keywords = ['python', 'python3', 'magnet'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'magpylib',
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)