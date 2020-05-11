/******************************
*
*  Module name : main.c
*  Version : 1.0
*  Purpose: Entry point module
*  Dated : 09-May-2020
*******************************/

#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<pthread.h>
#include<string.h>
int cook;
int students;
int tables;
int rounds;
int countersize;
int value;

pthread_t tid1,tid2,tid3,tid4;

//one run the file of supplier
void  *thread_function1(void *arg){
	printf("thread 1");
	char* args[] = {"supplier",NULL};
        char* command = "./supplier.o";
        execvp(command,args);
	pthread_exit(NULL);	

}
//run the file of cook
void *thread_function2(void *arg){
printf("thread 2");
	
	char* args1[] = {"help",NULL};
        char* command1 = "./help.o";
        execvp(command1,args1);
	pthread_exit(NULL);	

}
//run the file of students
void *thread_function3(void *arg){
printf("thread 3");

	char* args1[] = {"student",NULL};
        char* command1 = "./student.o";
        execvp(command1,args1);
	pthread_exit(NULL);	

}
//run the main file to share command line aurgument to other file
void *thread_function4(void *arg){
printf("thread 4");
       
	int f3=mkfifo("pipe_three",0664);
	int fifo_write3= open("pipe_three",O_WRONLY);
        write(fifo_write3,&value,4);



	int f4=mkfifo("pipe_four",0663);
	int fifo_write4= open("pipe_four",O_WRONLY);
	write(fifo_write4,&cook,4);     


	int f5=mkfifo("pipe_five",0660);
	int fifo_write5= open("pipe_five",O_WRONLY);
        write(fifo_write5,&students,4);
        write(fifo_write5,&rounds,4);
	
	pthread_exit(NULL);	

}



int main(int argc, char *argv[]) 
{ 
int i;
    if( argc >= 9 )
    {
        printf("The arguments supplied are:\n");       
	for(int i=0;i<argc;i++){
	
		if(strcmp(argv[i],"-N")==0){
			i++;
			cook=atoi(argv[i]);
					}
		if(strcmp(argv[i],"-T")==0){
			i++;
			tables=atoi(argv[i]);
					   }
		if(strcmp(argv[i],"-S")==0){
			i++;
			countersize=atoi(argv[i]);
			}
		if(strcmp(argv[i],"-L")==0){
			i++;
			rounds=atoi(argv[i]);
			}
		if(strcmp(argv[i],"-U")==0){
			i++;
			students=atoi(argv[i]);
			}
		if(strcmp(argv[i],"-G")==0){
			i++;
			students+=atoi(argv[i]);
			}
		if(strcmp(argv[i],"-M")==0){
			i++;
			students=atoi(argv[i]);
			}
			}
       		value=rounds*students*3;

       
       
       		printf("%d\n",cook);
       		printf("%d\n",students);
       		printf("%d\n",tables);
      		printf("%d\n",countersize);
       		printf("%d\n",rounds);
       		printf("%d\n",value);
             
    }
    else
    {
        printf("argument list is empty.\n");
        return 0;
    }

int a=fork();
int message1,message2;
if(a==0){
	//first thread
	pthread_create(&tid1,NULL,thread_function1,NULL);

}
	else{
	int b=fork();
		if(b==0){
			//second thread
			pthread_create(&tid2,NULL,thread_function2,NULL);
			}
		else{
			int c=fork();
			if(c==0){
				//third thread
				pthread_create(&tid3,NULL,thread_function3,NULL);
				}
			else{
				//four thread
       				pthread_create(&tid4,NULL,thread_function4,NULL);
}

}
}

  		pthread_exit(NULL);
		return 0; 
} 


