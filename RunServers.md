# Running the boolserver
For getting the system online one has to do the following
+ Clone all the repos from [http://github.com/boolserver](http://github.com/boolserver) in respective server. For running on the same machine clone all the repos in the system using `git clone <repo name>`
* In each repo run the command `make` to compile the codes. On the frontend server(if running seperatly) you might also have to install `uuid-dev`. For that run `sudo apt-get install uuid-dev`
* For running the msg queue and backend server simpily type `make run`
* For the frontend, you would need 2 instances of terminal. In each type `make run_client_frontend` and `make run_backend_frontend`
* For the user/client type `./client.out <mode> <input> <optional>`. For more details run `./client.out`, this will print out the info on the commands
