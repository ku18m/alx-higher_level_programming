#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to list to be checked.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 * OR 2 if it failed.
 */
int is_palindrome(listint_t **head)
{
	int len, *tmp, i;
	bool flag = 0;
	listint_t *check;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	check = *head, len = 0;
	while (check)
	{
		check = check->next;
		len++;
	}
	if (len % 2 == 0)
		len = len / 2;
	else
		len = (len - 1) / 2, flag = 1;
	tmp = (int *)malloc(len * sizeof(int));
	if (tmp == NULL)
		return (2);
	check = *head, i = 0;
	while (i < len)
		tmp[i] = check->n, check = check->next, i++;
	i = len - 1;
	if (flag == 1)
		check = check->next;
	while (i >= 0)
	{
		if (check->n != tmp[i])
			return (0);
		check = check->next;
		i--;
	}

	free(tmp);
	return (1);
}
