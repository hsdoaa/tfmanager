from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='tfmanager',
      version='1.0.0',
      description='A text file manger',
      long_description=long_description,
      url='https://github.com/hsdoaa/tfmanager',
      author='Doaa Hassan Salem',
      author_email='hsdoaa@gmail.com',
      license='MIT',
      packages=['tfmanager'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='text file mangement'
      )
