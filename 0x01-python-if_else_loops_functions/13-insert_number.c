#include "lists.h"

/**
 * insert_node - check the code
 * @head: the list
 * @number: the # to insert
 * Return: the newnode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *next = *head;
	listint_t *newNode;
	int n;
	int nn;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	if (number == 0 && *head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	else if (number == 0 && *head != NULL)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (next != NULL && next->next != *head)
	{
		n = newNode->n;
		nn = next->next->n;
		if (n >= next->n && (n <= nn || next->next == NULL))
		{
			temp = (next)->next;
			(next)->next = newNode;
			newNode->next = temp;
			return (newNode);
		}
		next = next->next;
	}
	free(newNode);
	return (NULL);
}
