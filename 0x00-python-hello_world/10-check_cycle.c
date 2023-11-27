#include <stdlib.h>

/* Define the structure for a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list) {
    listint_t *slow_ptr, *fast_ptr;

    if (list == NULL || list->next == NULL) {
        /* If the list is empty or has only one node, there is no cycle. */
        return 0;
    }

    slow_ptr = list;
    fast_ptr = list->next;

    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        if (slow_ptr == fast_ptr) {
            /* If slow_ptr and fast_ptr meet, there is a cycle. */
            return 1;
        }

        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }

    /* If the loop completes without meeting, there is no cycle. */
    return 0;
}
