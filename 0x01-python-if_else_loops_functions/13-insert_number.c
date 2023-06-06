#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new element into a list
 *
 * @head: the head of the list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *next, *new;

	if (head == NULL)
		return (NULL);

	while ((*head) != NULL && (*head)->n < number)
		head = &(*head)->next;

	next = *head;
	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = next;
	*head = new;

	return (new);
}
