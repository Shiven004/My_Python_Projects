/********************************
*
*  Module name : supplier.c
*  Version     : 1.0
*  Purpose     : Supplier module
*  Dated       : 09-May-2020
*********************************/
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <stdio.h> 
#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<sys/stat.h>
int l;
int main(int argc, char *argv[]){
 //it takes capacity of kitchen plates from the  
 int f3=mkfifo("pipe_three",0664);
 int fifo_read3 = open ("pipe_three",O_RDONLY);
 read(fifo_read3,&l,4);
 //this pipe is used to send plates to kitchen
 int size;
 int f1=mkfifo("pipe_one",0666);
 int fifo_write= open("pipe_one",O_WRONLY);

if(fifo_write<0){
printf("\nerro in file opening\n");
}
else{
	for(int i=0;i<l;i++){
  		size=i%3;
 	if(size==0){
 		printf("Supplier is supplying soup to kitchen\n");
 		   }
 	if(size==1){
 		printf("Supplier is supplying desert to kitchen\n");
 		   }
 	if(size==2){
 		printf("Supplier is supplying maincourse to kitchen\n");
 }
 	write(fifo_write,&size,4);
 
 }
}
	size=10;
	write(fifo_write,&size,4);
	printf("\nSypplier has completed his/her work ..Good bye.. Going home\n");
}


