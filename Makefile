export
SHELL := /bin/bash

directory = venv

# all: | $(directory)
#     @echo "Continuation regardless of existence of ~/Dropbox"

# $(directory):
#     @echo "Folder $(directory) does not exist"
#     mkdir -p $@


build: | $(directory)
	@echo "installing venv and python packages"
	source ./venv/bin/activate; \
	pip install -r requirements.txt


$(directory):
	@echo "Folder $(directory) does not exist"
	virtualenv --no-site-packages -p python3 $@

run:
	source ./venv/bin/activate; \
	python main.py


# all:
#         @echo "Found ~/Dropbox."
#         @echo "Did not find ~/Dropbox."
# endif
