#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: pointer to list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}

	return (0);
}
