import os

from setuptools import find_packages, setup

with open(os.path.join("aml_rl", "version.txt")) as file_handler:
    __version__ = file_handler.read().strip()


long_description = """

# Advanced Machine Learning

This project is our semester project for CSCI 5525 at the University of Minnesota. Our aim is to develop
reiforcement learning algorthms for performing pick and place operations with a simulated robotic arm.

"""  # noqa:E501


setup(
    name="https://github.com/padpy/aml_rl",
    packages=[package for package in find_packages() if package.startswith("https://github.com/padpy/aml_rl")],
    package_data={"stable_baselines3": ["py.typed", "version.txt"]},
    install_requires=[
        "gym==0.21",  # Fixed version due to breaking changes in 0.22
        "numpy",
        "torch>=1.11",
        'typing_extensions>=4.0,<5; python_version < "3.8.0"',
        # For saving models
        "cloudpickle",
        # For reading logs
        "pandas",
        # Plotting learning curves
        "matplotlib",
        # gym and flake8 not compatible with importlib-metadata>5.0
        "importlib-metadata~=4.13",
    ],
    extras_require={
        "tests": [
            # Run tests and coverage
            "pytest",
            "pytest-cov",
            "pytest-env",
            "pytest-xdist",
            # Type check
            "pytype",
            "mypy",
            # Lint code
            "flake8>=3.8",
            # Find likely bugs
            "flake8-bugbear",
            # Sort imports
            "isort>=5.0",
            # Reformat
            "black",
            # For toy text Gym envs
            "scipy>=1.4.1",
        ],
        "docs": [
            "sphinx",
            "sphinx-autobuild",
            "sphinx-rtd-theme",
            # For spelling
            "sphinxcontrib.spelling",
            # Type hints support
            "sphinx-autodoc-typehints==1.21.1",  # TODO: remove version constraint, see #1290
            # Copy button for code snippets
            "sphinx_copybutton",
        ],
        "extra": [
            # For render
            "opencv-python",
            # For atari games,
            "ale-py==0.7.4",
            "autorom[accept-rom-license]~=0.4.2",
            "pillow",
            # Tensorboard support
            "tensorboard>=2.9.1",
            # Checking memory taken by replay buffer
            "psutil",
            # For progress bar callback
            "tqdm",
            "rich",
        ],
    },
    description="University of Minnesota: Twin Cities CSCI 5525 course project",
    author="Antonin Raffin",
    url="https://github.com/padpy/aml_rl",
    author_email="nicholas.padilla@npcomplete.io",
    keywords="reinforcement-learning-algorithms reinforcement-learning machine-learning "
    "gym openai",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.7",
    # PyPI package information.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
