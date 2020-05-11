/*****************************
*
*  Module name: studen.c
*  Version    : 1.0
*  Purpose    : Student module
*  Dated      : 09-May-2020
*****************************/

#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <stdio.h> 
#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<sys/stat.h>
#define buffSize 1000
#include<semaphore.h>
int totaltable=4;
int capacity=3;
int kitchen;
int s=0;
int d=0;
int p=0;
int totalround=13;
int totalstudents=10;
sem_t sem; 
int fifo_read2;
//struct store student round and id
struct student{
	int id;
	int round;
	int waitftable;
};


//thread read data from counter so it decides weather it can get food from counter or not
void *thr_func(void *arg) {
  	struct student *data = (struct student *)arg;   
    	int value;
     	int saize=10;
    
    	sem_getvalue(&sem,&value);
    	if(value<=0 || data->round>=totalround){
    		return NULL;
    		printf("\nHello I am Student no: %d\n ", data->id);
   		printf("\n Saying Good bye\n");
    		return NULL;
    						}
  
    		read(fifo_read2,&saize,4);
    	if(saize==1){
    		printf("\n\n\nSystem\n");
    		printf("\nHello I am Student no: %d\n ", data->id);
    		sem_trywait(&sem);
    		sem_trywait(&sem);
    		sem_trywait(&sem);
    		data->round=data->round+1;
    		int senirio=(data->id)%totaltable;
    		printf(" eat food on table no %d round no %d  ",senirio,data->round );
    		value=value-3;
    		printf(" # kitchen items = %d\n",value);
    			if(data->round>=totalround){
    				printf("\nGood bye\n");
    						   }
   }
        else if(saize==0) {
    		printf("\nHello I am Student no: %d ", data->id);
    		printf(" waiting for food on counter  \n");
    
    }     
    saize=10;
}



int main(int argc, char *argv[]){

		//read from main file no of students Graduates and Under-Graduates ,and Rounds
		int f5=mkfifo("pipe_five",0660);
		int fifo_read5 = open ("pipe_five",O_RDONLY);
		int initial;
		read(fifo_read5,&initial,4);
		totalstudents=initial;
		read(fifo_read5,&initial,4);
		totalround=initial;
		kitchen=totalround*totalstudents*3;
		
		//read counter information from cook
		int f2=mkfifo("pipe_two",0665);
		fifo_read2 = open ("pipe_two",O_RDONLY);


		int i;
		struct student tstud[totalstudents];
		pthread_t thr[totalstudents];
		
		for(i=0;i<totalstudents;i++){
			tstud[i].id=i;
			tstud[i].round=0;
						}
		sem_init (&sem,0,kitchen);
 		int get=5;
		for(int k=0;get>0;k++){
 			sem_getvalue(&sem,&get);
			for (i = 0; i < totalstudents; i++) {
   					pthread_create(&thr[i], NULL, thr_func,&tstud[i]);
  							    }
  /* block until all threads complete */
  			for (i = 0; i < totalstudents; i++) {
    					pthread_join(thr[i], NULL);   
  							}}

}
