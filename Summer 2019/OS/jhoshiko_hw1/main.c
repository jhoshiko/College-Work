#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <assert.h>

/*
Joshua Hoshiko
CS3600
Project 1

Note: John Hall assisted with the creation of this code
*/

int main() {
    //Fork process
    pid_t pid = fork();

    //Make sure nothing broke during the fork
    if(pid < 0) {
        perror("Fork");
        exit(errno);
    }

    //Check to see if the process is the child. Then hand off 5
    //to counter
    else if(pid == 0) {
        char n[] = "5";
        execl("./counter", "counter", n, 0);
        exit(0);
    }

    //Check to see if the process is the parent. Print appropriate data
    //then return the status of counter, which should be n
    else {
        int status, returnedStatus
        int child = waitpid(pid, &status, 0);
        wait(&child);
        printf("My PID: %d\n", getpid());

        if(WIFEXITED(status)){
            returnedStatus = WEXITSTATUS(status);
            assert (printf("Process %d exited with status: %d\n",child, returnedStatus)!=0);
        }
    }

    return 0;
}
