#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while -  simple loop that runs indefinitely using a while loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry point to program
 * Return: 0 if successful
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			exit(0);
		}
		else
		{
			perror("fork error");
			return (1);
		}
	}

	infinite_while();

	return (0);
}
