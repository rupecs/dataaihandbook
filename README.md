![](./source/Images/homepage.png)

# Sphinx-with-Github-Pages
Sphinx-with-Github-Pages was born from the need for developers who are not documenting specialists to easily, quickly, and independently build their documentation via Sphinx.

## Introduction
Sphinx-with-Github-Pages is a tutorial Python package to teach you quick start Sphinx documenting in a single place — so you can focus on building the next big thing. This package helps all levels of Python developers and researchers for building their own Sphinx documentation and can be used through an interactive command-line interface (i.e. MacOS terminal or Windows command-line consoles) with little knowledge of Python.

Installation, Usage, documentation and scripts are described at
 https://maihao14.github.io/Sphinx-with-Github-Pages/

Author: [`Hao Mai`](https://www.uogeophysics.com/authors/mai/)(Developer and Maintainer)


## Installation

### Conda environment

We recommend creating a custom
[conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html)
where `Sphinx-with-Github-Pages` can be installed along with its dependencies.

- Create a environment called `sphinx` :

```bash
conda create -n sphinx python=3.8 -c conda-forge
```

- Activate the newly created environment:

```bash
conda activate sphinx
```

### Installing

Download or clone the repository:
```bash
conda install sphinx
pip install sphinx_rtd_theme
```

## Running the quickstart scripts

Create a work folder where you will run the scripts that accompany `Sphinx`. For example:

```bash
mkdir ~/DocsWorkFolder
cd DocsWorkFolder
```

Run `sphinx-quickstart`:

```bash
sphinx-quickstart
```

A `sphinx-quickstart` welcome interface will be loading:


## Contributing

All constructive contributions are welcome, e.g. bug reports, discussions or suggestions for new features. You can either [open an issue on GitHub](https://github.com/maihao14/Sphinx-with-Github-Pages/issues) or make a pull request with your proposed changes. Before making a pull request, check if there is a corresponding issue opened and reference it in the pull request. If there isn't one, it is recommended to open one with your rationale for the change. New functionality or significant changes to the code that alter its behavior should come with corresponding tests and documentation. If you are new to contributing, you can open a work-in-progress pull request and have it iteratively reviewed. Suggestions for improvements (speed, accuracy, etc.) are also welcome.
