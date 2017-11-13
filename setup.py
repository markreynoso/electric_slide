from setuptools import setup


setup(
    name="electric_slide",
    description="Command-line script used to track donations and \
    write thank you notes.",
    py_modules=['board'],
    install_requires=[

    ],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
