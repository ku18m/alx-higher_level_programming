#include <Python.h>

/**
 * print_elements - prints the elements of an object.
 *
 * @obj: the object to print.
 * @len: object length.
 *
 * Return: Nothing.
 */
void print_elements(long int len, PyListObject *obj)
{
	int i;

	for (i = 0; i < len; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 * @p: the object to print.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *obj = (PyListObject *)p;
	long int size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	print_elements(size, obj);
}
