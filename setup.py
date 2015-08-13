from distutils.core import setup


setup(
    name='typesafe-hints',
    version='1.0',
    description='Efficient general typesafety based on type hints.',
    author='Justus Adam',
    author_email='dev@justus.science',
    maintainer_email='dev@justus.science',
    platforms=['POSIX', 'Windows'],
    license='GPLv2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
    ],
    long_description='This package provides a simple decorator that will '
    'check the type of supplied arguments and return values of decorated '
    'functions on every call.',
    url='https://github.com/JustusAdam/python-typesafety',
    packages=['typesafe'],
    package_dir={'typesafe': 'src/typesafe'}
    )
