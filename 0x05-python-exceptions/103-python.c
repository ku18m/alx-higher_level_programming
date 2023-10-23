#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - print some basic info about Python bytes.
 *
 * @p: PyObject.
 *
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);

	i = 0;
	while (i < size)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
		i++;
	}
}

/**
 * print_python_float - print some basic info about Python float.
 *
 * @p: PyObject.
 *
 * Return: Nothing.
 */
void print_python_float(PyObject *p)
{
	char *content;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	content = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
								   Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", content);
	PyMem_Free(content);
}

/**
 * print_python_list - print some basic info about Python lists.
 *
 * @p: PyObject.
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	const char *tp_name;
	Py_ssize_t size, allocated, i;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocated = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		tp_name = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, tp_name);
		if (strcmp(tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(tp_name, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}
