#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - start
 *
 * @head: the node
 * @number: the data
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *curnt = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;
	while (curnt)
	{
		if (node->n <= curnt->next->n)
		{
			node->next = curnt->next;
			curnt->next = node;
			return (node);
		}
		else
		{
			curnt = curnt->next;
		}
	}
	return (NULL);
}
