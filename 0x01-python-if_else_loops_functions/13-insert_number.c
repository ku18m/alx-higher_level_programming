#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Pointer to list.
 * @number: The number to be inserted.
 *
 * Return: Created node address OR NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2, *new;
	int flag = 0;

	if (*head == NULL)
	{
		new = malloc(sizeof(listint_t *));
		if (!new)
		{
			free(new);
			return (NULL);
		}
		new->n = number, new->next = NULL;
		*head = new;
		return (new);
	}

	temp = *head, temp2 = *head;
	while (temp2)
	{
		if (temp2->n <= number && temp2->next == NULL)
		{
			flag = 1;
			break;
		}
		if (temp2->n > number)
		{
			flag = 2;
			break;
		}
		if (temp2->n <= number && temp2->next->n >= number)
		{
			flag = 3;
			break;
		}
		temp = temp->next;
		temp2 = temp->next;
	}

	new = malloc(sizeof(listint_t *));
	if (!new)
	{
		free(new);
		return (NULL);
	}

	new->n = number;
	if (flag == 1)
	{
		temp2->next = new;
		new->next = NULL;
	}
	else if (flag == 2)
	{
		*head = new;
		new->next = temp2;
	}
	else if (flag == 3)
	{
		new->next = temp2->next;
		temp2->next = new;
	}

	return (new);
}
