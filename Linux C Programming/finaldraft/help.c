/***************************
*
*  Module name : help.c
*  Version     : 1.0
*  Purpose     : Cook module
*  Dated       : 09-May-2020
****************************/
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
int fifo_write2;
int kitchen=0;
pthread_mutex_t lock_x;
sem_t sem ;

 int p=0;
 int s=0;
 int d=0;
 int c=2;
int capacity=3;
int p2=0;
int s2=0;
int d2=0;

//this function is used to check the capacity of counter
int checkcountercapacity(){
	int vl=1;
	if(p2+s2+d2<capacity){
		return vl;
			     }
	vl=0;
	return vl;
}

void *thr_func(void *arg) {
  	int *data = (int *)arg;
     	int value;
 	sem_getvalue(&sem,&value);
 	
       if(value<=0 && p<=0 && s<=0 && d<=0){
    		int saize=1;
    		write(fifo_write2,&saize,4);
    		printf("Hello I am cook no: %d\n", *data); 
    		printf("Good bye");
    		return NULL;
    		}
      if(p2>0 && s2>0 && d2>0){
      int saize=1;
      printf("\n\nSystem\n");
      write(fifo_write2,&saize,4);
      p2--;
      s2--;
      d2--;

    }
    else if(value>0){
    	int saize=0;
    	write(fifo_write2,&saize,4);
    	if(checkcountercapacity()==1 && (p>0 || s>0 || d>0 )){	
   
   		 if(p2==0){
    			p2++;
    			p--;
    			sem_trywait(&sem);
    			}
    		else if(s2==0){
    			s2++;
    			s--;
    			sem_trywait(&sem);
    				}
    		else if(d2==0){
    			d2++;
    			d--;
    			sem_trywait(&sem);
    				}
    
     		printf("Hello I am cook no: %d\n", *data);
    		printf(" # kitchen items = %d\n",value);
    				}
    
    				}
    	else{
     		printf("Hello I am cook no: %d\n", *data); 
   		printf("waiting for free the counter\n");
    		}
}


int main(int argc, char *argv[]){
 		int f4=mkfifo("pipe_four",0663);
		int fifo_read4 = open ("pipe_four",O_RDONLY);
 		int l;
 		int m;
 		int c;
 		int i=0; 
 		int a=0;
 		//pipe read no of cooks and capacity of kitchen from main 
 		read(fifo_read4,&c,4);
 		read(fifo_read4,&l,4);
 

 		int cook[c];
 		pthread_t thr[c];

 		//use to write or give dishes to student
		int f2=mkfifo("pipe_two",0665);
		fifo_write2= open("pipe_two",O_WRONLY);

 		//used to read dish from supplier 
 		int f1=mkfifo("pipe_one",0666);
 		int fifo_read = open ("pipe_one",O_RDONLY);
 		for(i=0;i<c;i++){
 			cook[i]=i;
 				}
		if(fifo_read<0){
			printf("Error opening file");
			       }
		else{
			int size;
 			for(i=0;size!=10;i++){
 				read(fifo_read,&size,4);
 					if(size==0){
 						s++;
 						kitchen=p+s+d;
 						 }
 					else if(size==1){
 						d++;
 						kitchen=p+s+d; 
 							}
 					else if(size==2){
 						p++;
 						kitchen=p+s+d;
 
 							} 
 						printf("\ntotal elements in kitchen  %d",kitchen);
 							}
 					sem_init (&sem,0,kitchen);

 					int get=5;
  					for(int k=0;get>0;k++){
  						sem_getvalue(&sem,&get);
  					for (i = 0; i < c; i++) {
   						pthread_create(&thr[i], NULL, thr_func, &cook[i]);
  								}
  						/* block until all threads complete */
  					for (i = 0; i < c; i++) {
    						pthread_join(thr[i], NULL);
  								}
								}}
 
}
