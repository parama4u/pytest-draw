from setuptools import setup, find_packages

setup(
    name='pytest-draw',
    version='0.1',
    packages=['pytest_draw'],
    entry_points={'pytest11': ['pytest_draw = pytest_draw.plugin']},
    url='https://github.com/parama4u/pytest-draw',
    author='Param',
    description='Pytest plugin for randomly selecting a specific number of tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email="parama4u@gmail.com",
    install_requires=[
        "pytest",
    ],
    classifiers= [
                "Development Status :: 3 - Alpha",
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
