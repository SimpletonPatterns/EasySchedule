# EasySchedule

[![Join the chat at https://gitter.im/SimpletonPatterns/EasySchedule](https://badges.gitter.im/SimpletonPatterns/EasySchedule.svg)](https://gitter.im/SimpletonPatterns/EasySchedule?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Development

To setup your virtualenv:

    $ mkvirtualenv easyschedule
    $ setvirtualenvproject easyschedule path_to_project

    # Optionally, create a new project with
    $ mkproject easyschedule
    $ git clone git@github.com:SimpletonPatterns/EasySchedule.git .

Then, every time you work on the project, run:

    $ workon easyschedule

To install the dependencies run:

    $ pip install -r requirements.txt
    # And the dev requirements
    $ pip install -r requirements-dev.txt

## Testing

To run the tests:

    # Install dev requirements (includes pytest)
    $ pip install -r requirements- dev.pip
    $ py.test

### Testing cheat-sheet:

    # See available fixtures
    $ py.test --fixtures
    # Run tests with stdout enabled
    $ py.test -s

The `pytest.ini` file contains the test configuration, including generation of a HTML test report to `htmlcov/report.html`

### Virtualenvwrapper cheat-sheet

    # To stop working
    $ deactivate
    # To show all environments
    $ workon
    # To show installed packages
    $ lssitepackages
