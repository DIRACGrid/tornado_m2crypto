from io import open
from os.path import dirname, join

from setuptools import setup


with open(join(dirname(__file__), 'README.md'), "rt") as fp:
    long_description = fp.read()


setup(
    name='tornado_m2crypto',
    use_scm_version=True,
    description="Extension for running tornado with M2Crypto instead of the standard python SSL module",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DIRACGrid/tornado_m2crypto',
    setup_requires=[
        'setuptools_scm<6; python_version < "3"',
        'setuptools_scm; python_version >= "3"',
    ],
    install_requires=[
        'enum34; python_version < "3.4"',
        # Upper pin: m2crypto 0.46.0 rewrote ssl_read() in src/SWIG/_ssl.i and inverted the
        # handling of ssl_sleep_with_timeout()'s return value (and dropped the gettimeofday()
        # that initialises the deadline). Any read() on a connection with a timeout set now
        # busy-loops and returns with a stale SSLTimeoutError set, which surfaces as
        # "SystemError: <built-in function ssl_read> returned a result with an exception set"
        # and breaks all DIRAC DISET/dips connections. Still unfixed upstream as of 0.49.0.
        ## Reported in
        ## https://lists.sr.ht/~mcepl/m2crypto/%3C7b94d866-bdd2-4a29-9713-b6a6fd076ad7@cta-observatory.org%3E
        'm2crypto >=0.43,<0.46',
        'tornado',
    ],
    packages=['tornado_m2crypto', 'tornado_m2crypto.test'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    keywords='dirac ',
    python_requires='>=2.7',
    extras_require={
        'testing': ['requests'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/DIRACGrid/tornado_m2crypto/issues',
        'Source': 'https://github.com/DIRACGrid/tornado_m2crypto/',
    },
)
