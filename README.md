# This script for auto generated documentation.
It works with **relative** and **absolute** paths,
and can work with several documents. Every class
with its methods,  every stand-alone functions
will be in the report with theirs docstring.
If there is no docstring the result will be None.
This report(filename_doc.txt) saves in same directory
that filename1.py.
How to run:
#### 1) Runs with **relative** paths 
```bash
python ~/pydoc_light.py  ~/filename1.py ~/filename2.py
```
#### 2) Runs with **absolute** paths 
```bash
python ~/pydoc_light.py /usr/bin/filename1.py /usr/bin/filename2.py
```
#### 3) Runs with **relative** and **absolute** paths 
```bash
python ~/pydoc_light.py ~/filename1.py /usr/bin/filename2.py
```
