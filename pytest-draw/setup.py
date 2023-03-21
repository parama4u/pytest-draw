from setuptools import setup

setup(
    name='pytest-draw',
    version='0.3',
    packages=['pytest-draw'],
    url='https://github.com/parama4u/pytest-sanity',
    author='Param',
    author_email="parama4u@gmail.com",
    py_modules=['pytest-draw/plugin'],
    entry_points={'pytest': ['pytest_sanity = pytest-draw/plugin']},
    install_requires=[
        "pytest>=5.0.0",

    ],
    classifiers= [
                "Development Status :: 1 - Planning",
                "Programming Language :: Python :: 3",
                "Framework :: Pytest",
                "Framework :: Robot Framework :: Library",
                "Intended Audience :: Developers",
                "Intended Audience :: Information Technology",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Topic :: Software Development :: Testing",
                "Topic :: Software Development :: Testing :: Acceptance",
                "Topic :: Software Development :: Testing :: Unit",
                "Topic :: Utilities"
    ],
)
