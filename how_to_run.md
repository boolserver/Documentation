# How to run the code

## Clone the Documentation repo
Run `git clone https://github.com/boolserver/Documentation.git`. This will create a repo that has the basic intialization code for setup of the system. Keep in mind this is done only in the case when we need all the servers to be running on the same machine that is for testing.

## Run the make command
There is a makefile that consists of some of the basic stuff that is required for the setup.
Running the command `make` will first install the required libraries, then it will clone the required repos that are needed. that is the repos for client, frontend, message queue and backend. NOTE:- sudo is required for installing the required libraries.

After the make command one must run `make run_make`. This will run the Makefile for each of the repos, forming the required executables.

## Running the all the servers
For running on the same machine, one must open 5 terminals. 3 terminals will correspond to client, msg queue and backend respectively. 2 terminals will run the 2 servers of the frontend, one is the serverside code for the client/user side the other is for the backend.

We do perform the following steps:-
* `cd` into the msg queue repo and run `make run` command. (This might need `sudo` as the POSIX msg queue requires it)
+ `cd` into the frontend repo and run `make run_client_frontend` & `make run_backend_frontend` on 2 seperate terminals
+ `cd` into the backend repo and run `make run`
+ `cd` into the clientside repo and run `./client.out <mode> <input> <optional>`, if one simply runs `./client.out` a msg will be printed that will give more details on the required parameters
