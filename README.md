# RPS Sim

A small console program that 'simulates' games of rock paper scissors.

## Installing

You need `pip`, as well as `pipenv`.

### Prerequisite: `pipenv`
If you don't yet have `pipenv`, first run:

```shell
$ pip install pipenv --user
```

For more information, see [the `pipenv` installation documentation](https://pipenv.pypa.io/en/latest/installation/).

### Installing RPS Sim

If only running the program, you should be able to install it like this:

```shell
$ pipenv shell
$ pipenv install
```

If looking to also develop, you will want to include the development dependencies in the package install, like so:

```shell
$ pipenv install --dev
```


## Running

Once installed, you should be able to run it with:

```shell
$ python ./rps-sim.py
```

## Tests

Assuming you have an active `pipenv` shell: 

```shell
$ pytest
```