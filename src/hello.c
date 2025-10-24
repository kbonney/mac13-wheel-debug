#include <Python.h>

static PyObject* hello(PyObject* self, PyObject* args) {
    return PyUnicode_FromString("Hello, macOS build!");
}

static PyMethodDef HelloMethods[] = {
    {"hello", hello, METH_NOARGS, "Say hello."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello",
    NULL,
    -1,
    HelloMethods
};

PyMODINIT_FUNC PyInit_hello(void) {
    return PyModule_Create(&hellomodule);
}
