#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This script for auto generated documentation.
    It works with relative and absolute paths,
    and can work with several documents. Every class
    with its methods,  every stand-alone functions
    will be in the report with theirs docstring.
    If there is no docstring the result will be None.
    This report(filename_doc.txt) saves in same directory
    that filename1.py.
    How to run:
    python ~/pydoc_light_2x.py  1)~/filename1.py ~/filename2.py
                                    OR
                              2)/usr/bin/filename1.py /usr/bin/filename2.py
                                    OR
                              3)~/filename1.py /usr/bin/filename2.py
"""
__author__ = 'om'
import sys
import types
import imp

from os import path


def main(path_to_file, num_import):
    """
        (EXAMPLE OF DOCSTRING)
        Name:;
        Input parameter: ;
        Output parameter: ;
        Work algorithm: ;
        Error code:
            «0» - ;
            «1» - ;
            «2» - ;
            «3» - ;
    """
    file_import = imp.load_source('module{0}'.format(num_import), path_to_file)
    count_class_and_function = 1
    count_method = 1
    # Takes filename without '.py'
    file_name = path.split(path_to_file)[1].split(".")[0]
    # Takes pathname without 'filename.py'
    path_name = path.split(path.abspath(path_to_file))[0]
    with open(path.join(path_name, "{0}_doc.txt".format(file_name)), 'w') as f:
        for doc_class in dir(file_import):
            if not doc_class.startswith("__"):
                if isinstance(type(getattr(file_import, doc_class)), types.ClassType):
                    # Print class name and its docstring
                    f.write("\n{0}) Имя класса: {1}\n".format(count_class_and_function, doc_class))
                    docstring = str(getattr(file_import, doc_class).__doc__).strip().split("\n")
                    for line in docstring:
                        f.write(line.strip() + "\n")
                    # Print method name and its docstring
                    for doc_method in dir(getattr(file_import, doc_class)):
                        if not doc_method.startswith("__"):
                            frm = "\n{0}.{1}) Имя метода: {2}\n"
                            f.write(frm.format(count_class_and_function, count_method, doc_method))
                            count_method += 1
                            docstring = str(getattr(getattr
                                                    (file_import, doc_class),
                                                    doc_method).__doc__).strip().split("\n")
                            for line in docstring:
                                f.write(line.strip() + "\n")
                    f.write("\n" + "|***|***" * 10 + "\n")
                    count_class_and_function += 1
                    count_method = 1
                # Print function name and its docstring
                if isinstance(type(getattr(file_import, doc_class)), types.FunctionType):
                    f.write("\n{0}) Имя функции: {1}\n".format(count_class_and_function, doc_class))
                    count_class_and_function += 1
                    docstring = str(getattr(file_import, doc_class).__doc__).strip().split("\n")
                    for line in docstring:
                        f.write(line.strip() + "\n")
                    f.write("\n" + "|***|***" * 10 + "\n")


if __name__ == "__main__":
    list_argv = sys.argv
    if len(list_argv) > 1:
        for i in range(1, len(list_argv)):
            main(list_argv[i], i)
