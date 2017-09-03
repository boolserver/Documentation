# Boolean Satisfiability Solver Server
In this project I develope an architecture that can be used for solving Boolean ANF Equations on a remote server, where client will provide the equations in ANF form to the frontend. The frontend will return a UUID which the client can use to check the status and, if complete, get the results in a txt file.

[boolserver](http://github.com/boolsserver) is the github organization project. The reason for diff repos for different is that one can `git clone <repo>` on various servers. So each server will have a different repo. But this has now given the problem for code repetation in multiple repos. Will be taking care of it soon.

## A little background
I am curently working with Prof. Virendra Sule of EE department on developing a new algorithm for Boolean SAT solver based on Implicant calculation. I was able to implement the solver in Python and we were able to break the bivium cipher for a given IV and some bits of clocking(We have submited the paper to a confrenece). The next step was to optimize the code and get better result. So using the techniqueues taught in CS 744, I sought to develop our solver, but due to pattening issues and still developement of the solver I can not share the code of the solver(which is the backend). Hence I have made an excutable for solver and also used that as part of my script running on the backend server. I will share the performance improvements and snippets of the solver code which show the use of optimization further down the line.

## Architecture
The current implementation of the system consists of 3 seperate servers and a client side code. The servers are
+ Frontend/Database
* Msg Queue
* Backend

As of now, due to time constrants I was not able to implement a full fledged database, but I will be implementing one before Phase 2. For now I am dumping all the data in `data/` directory in fronend server itself. The Backend will contact the frontend to get the required data<br>

## Basic Data flow
First the client creates a `json` file which consists of the ANF equations in array of array form. The table name for the equtions that he wants to solve in the json file should be `anf_equations`. Once he has the equations(from any source), he sends them to the frontend server. The frontend creates a random 16 byte UUID(This is converted to string of length 32 char) and returns it to the client. Then frontend stores the json file in `data/` directory with the name `<UUID>.json` and connection with the client is closed. The UUID is then transfered to the msg queue server.<br>

Now as and when the backend server is free it requests a UUID from the msg queue server, then the backend sends the UUID to the frontend server and recevies the corresponding Json file and stores it in `tmp_data/` dir on the backend. It then uses the `boolean_solver` executable to solve the equations in the json file with table name `anf_equations`. The results is also dumped into `tmp_data/` with filename as `<UUID>.txt`. Once the result file is formed the backend sends it to the frontend where it is stored in `data/` as `<UUID>.txt`. Then the backend server deletes the json and txt file from its `tmp_data/` dir and asks for another UUID from the msg queue. If the msg queue is empty the backend for now goes to sleep for 5 secs and then again askes for a UUID from msg queue<br>

The client can contact the frontend using the UUID to retrive its result file. Once the client has taken his corresponding result file, the frontend also deletes both json and txt files.

### Client
The client can send 2 types of requests for now
+ Sending a json file with equations for solving
* Retriving the results for the file using UUID

### Frontend
The frontend runs 2 sockets instances with different ports, one for handling incoming and outgoing data from the users/clients and other tranfering data to and from the backend server. Apart from this it also has a client side code sending data to msg queue server which is called in server instance for handling incoming data from users/clients.

The server frontend server as of now does not incorporate multiple clients, this is due to the fact that it has to take a file from each client and write it into the disk before sending corresponding UUID to msg queue. Since read write buffer is single, there was no point for making the frontend concurrent. This issue will be resolved when I use a standard database for handling file systems.

### Message Queue
I have used the POSIX MESSAGE QUEUE API for C for maintaing a msg queue. A server instance is used for handling 2 types of requests
+ Receving UUID to be entered in the Msg queue from frontend
* Sending UUID to the Backend server
Both, Backend and Frontend use client side codes for data transfer using approprite identifiers

### Backend
Backend uses `boolean_solver` executable that was formed using the C++ implementation of the Boolean Solver that I had done as part of this project only. I achived a speed up of 12x compared to python implementation of the solver. As of now there is no optimization done in the C++ code that could be worth noting. It is just a very crude transilation from python to C++. Apart from the solver, the backend consists of 2 clientside scripts one for the msg queue server for obtaining the UUID, and other for data tranfer to and from frontend server using appropriate identifiers.

## Future Work
Alot of the asspects I was not able to design and implement for this phase but here are a list of essintial features that will be added before phase 2
+ Database :- Will be including a standard database for handling files from the clients. There will a seperate server for the database
* MultiClient :- Once the a good database is implemented for file handling, making the Frontend server multithreaded will easy and make some sense
* Prallel Solver :- I will be paralleizing the boolean solver (which is in C++) first using `openmp` and later by `pthreads`

## Cutting Down Phase 0
Formation of ANF equations for Bivium Cipher was part of the report for Phase 0. I have the python code for creating the ANF equations for a given Key, IV and number of clocking cycles; generating a json file that can be solved by the Solver to obtain the key. I will be implimenting this is C++ and making another backend server. This way the client can provide a key and IV and produce the json file for ANF equations.<br>
I wont be able to complete this part of the project as this will take alot of time and I wont be able to work on further phases of the project. So from here on I will assume that the user/client will the ANF equations in the required format.
