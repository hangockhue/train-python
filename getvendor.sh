#!/bin/sh
set -eux
python3 -m pip download --no-binary :all: pycodestyle

tar xzf pycodestyle-*.tar.gz -C vendor/ 'pycodestyle-*/pycodestyle.py'
mv vendor/pycodestyle*/pycodestyle.py vendor/pep8.py
