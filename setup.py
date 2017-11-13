from setuptools import setup


setup(
    name="electric_slide",
    description="Machine learning project to solve slider puzzles.",
    py_modules=['board'],
    install_requires=[

    ],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
