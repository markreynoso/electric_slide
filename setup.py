import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'ipython',
    'pyramid_ipython',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
    'pytest-watch',
    'tox',
]

setup(
    name='electric_slide',
    version='1.0.0',
    description='electric-slide',
    py_modules=['board'],
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Megan Flood, Nathan Moore, Joseph Kim, Mark Reynoso',
    author_email='electric_slide@learn.ninja',
    url='https://electric-slide.herokuapp.com/',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = electric_slide:main',
        ],
        'console_scripts': [
            'initdb = electric_slide.scripts.initializedb:main',
        ],
    },
)
