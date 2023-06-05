#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * print_listint - returns  all the  element  of the  listint_t list
 * @h: point to the  head of the  list
 * Return: number of the  node
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; 

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - add newNode at  beginning of a listint_t list
 * @head: point to  pointer of the start of the list
 * @n: int to be included in the  node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - free  the listint_t list
 * @head: point to the  list to be freed
 * Return: nothing or void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
