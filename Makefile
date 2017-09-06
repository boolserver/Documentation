# Make file for running python script for clone, status, pull, push, make requests

status:
	python status_push_pull.py status

pull:
	python status_push_pull.py pull

push:
	python status_push_pull.py push

make:
	python status_push_pull.py make

clone:
	python status_push_pull.py clone
