#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singlyLinkedList
 * @n: int
 * @next: points to the nextNode
 * DONE BYT TEMESGEN ABDISSA
 * Description: singlyLinkedListNodeStructure
 * for ALX project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif 
