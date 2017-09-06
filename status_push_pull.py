# A python script for git status, pull, push for a given set of dirs

import os
import sys

def git_pull_status_push(dirs, mode):
    for d in dirs:
        print "\nMode -> %s for Directory -> %s" % (mode, d)
        if mode == "pull":
            os.system("cd %s && git pull origin master && cd -" % d)
        elif mode == "push":
            os.system("cd %s && git push origin master && cd -" % d)
        elif mode == "status":
            os.system("cd %s && git status && cd -" % d)

def git_clone_except_documentation(git_repos):
    print "Starting the cloning process of all the repos"
    for repo in git_repos:
        os.system("cd .. && git clone %s && cd -" % repo)

def run_make_file_for_all_dirs(dirs):
    for d in dirs:
        if d != "../Documentation/":
            os.system("cd %s && make && cd -" % d)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Too few parameters, define some mode...."
    else:
        mode = sys.argv[1]

    dirs = ["../backend_server/", "../clientside_server/", "../Documentation/", "../frontend_server/", "../message_queue/"]
    
    git_repo = [ \
        "https://github.com/boolserver/frontend_server.git", \
        "https://github.com/boolserver/clientside_server.git", \
        "https://github.com/boolserver/backend_server.git", \
        "https://github.com/boolserver/message_queue.git" \
    ]

    if mode in ['status', 'pull', 'push']:
        git_pull_status_push(dirs, mode)
    elif mode == "clone":
        git_clone_except_documentation(git_repo)
    elif mode == "make":
        run_make_file_for_all_dirs(dirs)
