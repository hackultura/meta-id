.PHONY: pyenv tox run test setup

pyenv:
	@export PYENV_ROOT=$PWD/.tox/.pyenv
	@pyenv install 2.7.9 -s
	@pyenv install 3.3.0 -s
	@env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.4.3 -s
	@pyenv install 3.5.0 -s
	@pyenv local 2.7.9 3.3.0 3.4.3 3.5.0

tox: pyenv
	@pyenv rehash
	@tox

test:
	@python manage.py test

setup:
	@pip install -r requirements.txt
