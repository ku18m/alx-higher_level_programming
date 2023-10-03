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

	if (head == NULL)
		return (NULL);

	temp = *head, temp2 = *head;
	while (temp2)
	{
		if (temp2->n <= number && temp2->next->n >= number)
			break;
		temp = temp->next;
		temp2 = temp->next;
	}

	new = malloc(sizeof(listint_t *));
	if (!new)
	{
		free(new);
		return (NULL);
	}

	new->next = temp2->next;
	new->n = number;
	temp2->next = new;

	return (new);
}
