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
	listint_t *temp, *next_temp;

	if (list == NULL)
		return (0);

	temp = list->next, next_temp = temp->next;
	while (temp != NULL && next_temp->next != NULL && next_temp->next->next)
	{
		if (temp == next_temp)
			return (1);
		temp = temp->next;
		next_temp = next_temp->next->next;
	}

	return (0);
}
