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
	if (!*head || number < 0)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (curnt->next != NULL && node->n > curnt->next->n)
	{
        	curnt = curnt->next;
	}
	node->next = curnt->next;
	curnt->next = node;
	return (node);
}
