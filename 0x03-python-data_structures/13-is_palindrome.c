#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - characters that reads the same forwards as backward
 * @head: the node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arry, *reverarry;
	int size = 0, i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (current != NULL)
	{
		size++;
		current = current->next;
	}
	arry = malloc(size * sizeof(int));
	current = *head;
	for (i = 0; i < size; i++)
	{
		arry[i] = current->n;
		current = current->next;
	}
	reverarry = malloc(size * sizeof(int));
	for (i = size - 1, j = 0; i >= 0; i--, j++)
	{
		reverarry[j] = arry[i];
	}
	for (i = 0; i < size; i++)
	{
		if (arry[i] != reverarry[i])
		{
			free(arry);
			free(reverarry);
			return (0);
		}
	}
	free(arry);
	free(reverarry);
	return (1);
}
