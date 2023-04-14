![CI](https://github.com/padpy/aml_rl/actions/workflows/ci.yml/badge.svg)
# Advanced Machine Learning: Reinforcement Learning Project

This project is our semester project for CSCI 5525 at the University of Minnesota. Our aim is to develop
reinforcement learning algorithms for performing pick and place operations with a simulated robotic arm.

## Bootstrap
To bootstrap, download this repository and run the `./script/bootstrap`. This installs the other project repositories
required to perform training and installs them into your python environment. It is recommended to use a python environment
manager like virtualenv or conda.

```bash
# Install dependencies
./script/bootstrap
pip install -e .
```

## Updating Dependencies
If there are changes to the dependencies then you can update all of them by runing `script/update`.
```bash
./script/update
```

## Training
In the scripts directory, there are examples of how to run training. `script/trainDQN` trains a DQN model on the
PandaGraspDenseDiscrete-v3 task. To change the episode length, edit MAX_EPISODE_STEPS in
`deps/panda-gym/panda_gym/__init__.py`.

## Before you commit
### Linting and Style Check
Before committing make sure to run linting and style check. You can easily do so using the following make commands.

```bash
make lint
make check-codestyle
```

If you see any style mistakes try to correct them, ignore them using comments or style exceptions, or autoformat
the code using `black`.

```bash
make commit-check
```
