#include <Python.h>

void print_python_list(PyObject *p)
{
	int size = (int)PyList_Size(p);
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = item->ob_type->tp_name;

		printf("Element %d: %s\n", i, item_type);
	}
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	int size = (int)PyBytes_Size(p);
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (size >= 10)
		size = 10;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", bytes->ob_sval[i] & 0xff);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
