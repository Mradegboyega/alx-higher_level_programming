#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = Py_SIZE(p);
	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;

	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  Size: %ld\n", size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	bytes_str = PyBytes_AsString(p);
	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x", bytes_str[i] & 0xff);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

