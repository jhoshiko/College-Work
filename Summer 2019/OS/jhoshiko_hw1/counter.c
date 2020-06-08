#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

/*
Joshua Hoshiko
CS3600
Project 1

Note: John Hall assisted with the creation of this code
*/

int counter(int argc, char* argv[]) {
    //Cast argument n into integer
    char * val = argv[1];
    int n = (int)strtol(val,(char **)NULL,10 );

    //Check print status is not 0
    assert (printf("Child PID: %d\n", getpid())!=0);
    assert (printf("Parent PID: %d\n", getppid())!=0);

    //Print process data n times
    int i;
    for(i = 0; i < n; ++i){
        assert (printf("Process: %d %d\n", getpid(), i+1)!=0);
    }
    exit(n);
}
