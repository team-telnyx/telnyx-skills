.PHONY: venv install serve-setup serve start-dramatiq
UNAME := $(shell uname)
venv:
ifeq ($(UNAME), Windows)
	py -3 -m venv venv;
else
	python3 -m venv venv
endif
install: venv
ifeq ($(UNAME), Windows)
	venv\Scripts\activate.bat; \
	pip3 install -r requirements.txt;
else
	. venv/bin/activate; \
	pip3 install -r requirements.txt;
endif

serve-setup:
	python3 manage.py migrate;

serve:
	python3 manage.py runserver  0.0.0.0:8000

start-dramatiq:
ifeq ($(UNAME), Windows)
	venv\Scripts\activate.bat; \
	python3 manage.py rundramatiq;
else
	. venv/bin/activate; \
	python3 manage.py rundramatiq;
endif
