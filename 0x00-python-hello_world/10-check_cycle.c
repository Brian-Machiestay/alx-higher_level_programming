#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check the code
 * @list: the list to check
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *headaddr = list;
	listint_t *listcopy = list;
	int i;

	for (i = 0; listcopy->next != NULL; i++)
	{
		if (listcopy->next == headaddr)
			return (1);
		listcopy = listcopy->next;
	}
	return (0);
}
