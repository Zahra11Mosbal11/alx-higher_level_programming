#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check the code
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *end = list;

	while (end && end->next)
	{
		first = first->next;
		end = end->next->next;
		if ( first == end)
			return (1);
	}
	return (0);
}
