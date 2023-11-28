#include <stdio.h>
#include <stdlib.h>

/* Define the structure for a singly linked list node */
typedef struct listint {
    int data;
    struct listint *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  /* Memory allocation failed */
    }

    /* Initialize the new node */
    new_node->data = number;
    new_node->next = NULL;

    /* If the list is empty or the new node should be inserted at the beginning */
    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the correct position to insert the new node */
    current = *head;
    prev = NULL;
    while (current != NULL && current->data < number) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node into the list */
    prev->next = new_node;
    new_node->next = current;

    return new_node;
}

/* Function to print the elements of the linked list */
void print_list(listint_t *head) {
    while (head != NULL) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}
