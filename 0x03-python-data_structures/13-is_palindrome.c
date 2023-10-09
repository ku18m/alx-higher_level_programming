#include "lists.h"

/**
 * reverse_listint - reverse the given linked list.
 *
 * @head: pointer to list to be reversed.
 *
 * Return: Nothing.
 */
void reverse_listint(listint_t **head)
{
	listint_t *check1 = NULL;
	listint_t *tmp = *head;
	listint_t *check2 = NULL;

	while (tmp)
	{
		check2 = tmp->next;
		tmp->next = check1;
		check1 = tmp;
		tmp = check2;
	}
	*head = check1;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to list to be checked.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *check1, *check2, *half, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	check1 = *head, check2 = *head, half = NULL;
	while (true)
	{
		check2 = check2->next->next;
		if (!check2)
		{
			half = check1->next;
			break;
		}
		if (!check2->next)
		{
			half = check1->next->next;
			break;
		}
		check1 = check1->next;
	}
	reverse_listint(&half);
	tmp = *head;
	while (half && tmp)
	{
		if (tmp->n != half->n)
			return (0);
		half = half->next;
		tmp = tmp->next;
	}

	return (1);
}
