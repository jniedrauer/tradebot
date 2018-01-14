# vim: set noet

build: rpm tgz wheel

rpm:
		python setup.py bdist_rpm

tgz:
		python setup.py sdist

wheel:
		python setup.py bdist_wheel

.PHONY: build rpm tgz wheel
