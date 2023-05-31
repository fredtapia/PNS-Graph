from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'P-graph Algorithms for Process Network Syntheis'
LONG_DESCRIPTION = 'The translation of P-graph algorithms (MSG, SSG) to Python. Comes with the default LP model'

setup(name='pnsgraph',
      version='0.0.2'
      description='P-graph Algorithms for Proces network synthesis',
      author='John Frederick D. Tapia',
      author_email='john.frederick.tapia@dlsu.edu.ph',
      packages = find_packages(),
      install_requires=['pulp', 'itertools'],  # add any additional packages that
      # needs to be installed along with your package. Eg: 'car'

      keywords=['P-graph', 'Process Network Syntheis}'],
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
      ]
      )
