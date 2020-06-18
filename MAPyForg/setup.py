from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Natural Language :: Portuguese (Brazilian)',
  'Topic :: Software Development :: Libraries'
]

setup(
  name='MAPyForg',
  version='0.0.1',
  description='Biblioteca para integrar Forge e Power BI',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='João Martins',
  author_email='jpornelas@poli.ufrj.br',
  license='MIT',
  classifiers=classifiers,
  keywords='Forge',
  packages=find_packages(),
  install_requires=['']
)