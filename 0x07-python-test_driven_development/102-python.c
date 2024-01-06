#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    const char *value;
    PyObject *unicode;

    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsUTF8AndSize(p, &length);

    fprintf(stderr, "[.] string object info\n");
    fprintf(stderr, "  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    fprintf(stderr, "  length: %ld\n", length);
    fprintf(stderr, "  value: %s\n", value);
}

int main(void) {
    PyObject *s1, *s2, *s3, *s4, *s5, *s6, *s7;

    Py_Initialize();

    s1 = PyUnicode_DecodeUTF8("The spoon does not exist", 24, "strict");
    s2 = PyUnicode_DecodeUTF8("ложка не существует", 19, "strict");
    s3 = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, "strict");
    s4 = PyUnicode_DecodeUTF8("勺子不存在", 5, "strict");
    s5 = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, "strict");
    s6 = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, "strict");
    s7 = PyBytes_FromString("The spoon does not exist");

    print_python_string(s1);
    print_python_string(s2);
    print_python_string(s3);
    print_python_string(s4);
    print_python_string(s5);
    print_python_string(s6);
    print_python_string(s7);

    Py_DECREF(s1);
    Py_DECREF(s2);
    Py_DECREF(s3);
    Py_DECREF(s4);
    Py_DECREF(s5);
    Py_DECREF(s6);
    Py_DECREF(s7);

    Py_Finalize();

    return 0;
}

