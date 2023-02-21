![CI](https://github.com/padpy/aml_rl/actions/workflows/ci.yml/badge.svg)
# Advanced Machine Learning: Reinforcement Learning Project

This project is our semester project for CSCI 5525 at the University of Minnesota. Our aim is to develop
reinforcement learning algorithms for performing pick and place operations with a simulated robotic arm.


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
