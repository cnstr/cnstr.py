# Contributing

Contributing to this repository is simple.

1. [Setup a virtual env]

1. Install all project dependencies (in `requirements.txt`)

        pip install -Ur requirements.txt

1. Edit any files that you deem necessary to integrate your feature/fix

    Be sure to adhere to the coding style of the project when adding
    your feature/fix (comments, docstrings, etc)

1. Test your changes with various scripts

    Check the `scripts` directory for scripts to use

    When in doubt, use `scripts/time-test.py` to test your changes

1. Create your pull request with your changes

Keep in mind that when changing documentation, **you should NOT** generate
documentation before pushing your changes to your branch; the repository
contains an action that will do this when your pull request is merged

[Setup a virtual env]: https://docs.python.org/3/library/venv.html
