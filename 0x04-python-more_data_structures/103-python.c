#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print some basic info about python bytes objects.
 *
 * @p: Pyobject to print.
 *
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int len, i, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", str);
	if (len >= 10)
		max = 10;
	else
		max = len + 1;
	printf("  first %ld bytes:", max);
	for (i = 0; i < max; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	printf("\n");
}

/**
 * print_python_list - print some basic info about python lists.
 *
 * @p: Pyobject to print.
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	long int len, i;
	PyListObject *list;
	PyObject *obj;

	len = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < len; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
