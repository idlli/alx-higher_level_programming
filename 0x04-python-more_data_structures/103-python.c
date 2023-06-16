#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_bytes - prints info about a python bytes object
 *
 * @p: the python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *obj = (PyBytesObject *)p;
	long len = obj->ob_base.ob_size;
	int i;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", obj->ob_sval);
	len = len > 10 ? 10 : len;
	printf("  first %ld bytes:", len);
	for (i = 0; i < len; i++)
		printf(" %02x", obj->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_list - prints info about a python list
 *
 * @p: the python list
 */
void print_python_list(PyObject *p)
{
	PyObject *elem;
	Py_ssize_t i, len;

	if (p == NULL)
		return;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	i = 0;
	while (i < len)
	{
		elem = PyList_GET_ITEM(p, i);
		Py_INCREF(elem);
		printf("Element %ld: %s\n", i, elem->ob_type->tp_name);
		Py_DECREF(elem);
		i++;
	}
}
