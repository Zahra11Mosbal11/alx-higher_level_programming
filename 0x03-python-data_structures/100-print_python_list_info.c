#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, aloc, i;
	PyObject *ob;

	size = Py_SIZE(p);
	aloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", aloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		ob = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
