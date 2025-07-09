.PHONY: all install build clean

all: install build

install:
	pip install .

build:
	cd collector && mvn clean package

clean:
	pip uninstall otkt
	cd collector && mvn clean
