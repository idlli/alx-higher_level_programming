#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a cycle
 *
 * @list: the head of the list
 *
 * Return: 1 if there was a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);
	while (slow->next && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
