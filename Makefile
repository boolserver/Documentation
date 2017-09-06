# Make file for running python script for clone, status, pull, push, make requests

HOMEDIR=../

all: require create_dirs
	echo "Run with command -> status, pull, push, run_make or clone" 

create_dirs:
	cd $(HOMEDIR) && mkdir -p backend_server/tmp_data frontend_server/data && cd -

require:
	sudo apt-get install uuid-dev

status:
	python status_push_pull.py status

pull:
	python status_push_pull.py pull

push:
	python status_push_pull.py push

run_make:
	python status_push_pull.py make

clone:
	python status_push_pull.py clone
