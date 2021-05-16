from setuptools import setup

setup(
    name="atlas",
    version="0.1.0",
    description="A.T.L.A.S: Advanced Technology Leading All Sapiens",
    author="Killian Mathieu",
    py_modules=["atlas"],
    install_requires=["Click", "ccxt", "numpy"],
    extras_require={
        "dev": ["pytest", "pytest-mock"],
    },
    entry_points={
        "console_scripts": [
            "atlas = atlas:main",
        ],
    },
)
