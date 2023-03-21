# pytest-draw

Pytest plugin for randomly selecting a specific number of tests.

## Overview

`pytest-draw` is a pytest plugin that allows you to randomly select a specific number of tests from your test suite. This can be useful for running a smaller subset of your tests during development or as part of your continuous integration (CI) pipeline.

By default, `pytest-draw` selects 5 tests to run.

## Use Cases

Some potential use cases for `pytest-draw` include:

- Running a smaller subset of your tests during development to speed up iteration time
- Running a specific set of tests as part of your CI pipeline to ensure compatibility with certain environments or configurations
- Running tests randomly to catch flaky tests or race conditions

## Installation

You can install `pytest-draw` using `pip`:

` pip install pytest-draw `


## Usage

Once installed, you can use the `--draw` command-line option to specify the number of tests to randomly select. For example, to randomly select 10 tests from your test suite, you can run:

`` pytest --draw=10 ``

By default, `pytest-draw` selects 5 tests. You can specify a different number of tests using the `--draw` option. 

## Benefits

Some benefits of using `pytest-draw` include:

- Faster iteration time during development by running a smaller subset of your tests
- Improved test coverage by running tests randomly to catch flaky tests or race conditions
- Improved reliability of your CI pipeline by running a specific set of tests in certain environments or configurations

## How to Contribute

If you would like to contribute to `pytest-draw`, you can do so by opening a pull request on GitHub. We welcome contributions in the form of bug reports, feature requests, and code changes.

To get started, clone the `pytest-draw` repository and install the development dependencies:


We appreciate your contributions to `pytest-draw` and thank you for your support!

## License

`pytest-draw` is licensed under the [MIT](https://opensource.org/license/mit/) License. 
