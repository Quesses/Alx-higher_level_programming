#include "Python.h"

/**
 * print_python_list_info - prints python information
 * Description:
 * prints information about a given vpython list
 * Format:-
 * [*] Size of the Python List is x
 * [*] Allocated = x
 * List of items with their type
 *
 * @p: pointer to the given list
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size;
	Py_ssize_t i = 0;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		while (i < size)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
			i++;
		}
	}
}
