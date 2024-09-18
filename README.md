# Introduction

***
It is a Python packadge that can help you obtain target files, and save the files and the corresponding paths as a list.

# Quick start

***

## Installation

Download walkTF from github, and then enter 'walkTF/dist':
```
cd walkTF/dist
```
and enter this command in command line:
```
pip install walkTF-1.0-py3-none-any.whl
```

## Use
Create a python script, and use this packadge.
```python
from walkTF import walk_target_files
print(walk_target_files())
```
It will output all files in current direction if you do not give any parameters.
The result is a list of [(file_root, file), (file_root, file), (file_root, file), (file_root, file), ..., (file_root, file)]
