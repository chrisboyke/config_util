# config_util.py

## Overview

A quick and easy way to have your python script be configurable via an .INI file, rather than by command-line arguments.  __config_util__ makes it easy to add .INI support by adding a single line to your script, and takes care of things like:
- Finding the right .INI file to load,  following a few common-sense rules
- Handling nesting of .INI files ("includes")

## Installation

1. Clone or download this project to a project folder (i.e. /opt/projects/config_util)
2. Set your PYTHON_PATH variable to point to this folder.  
For example, in your ~/.bashrc, add the following line:

```bash
export PYTHON_PATH=/opt/projects/config_util
```

## Usage

Add this as the first line of your "main" function, like this:

```python
def main():
    config = config_util.read_config()
```

The returned value is a standard ConfigParser object, which is widely used and extensively documented:

https://docs.python.org/3/library/configparser.html

## .INI Filename / Location

If a command-line parameter is passed to your script, then  __config_util__ will assume that this is the .INI filename.  For example, if you run:

```bash
$ some_script.py foo.ini
```

 __config_util__ opens and reads __foo.ini__

If no argument is passed in, then  __config_util__ assumes that an .INI file with the same basename as your script is to be used.  For example, if you run:

```bash
$ some_script.py
```

 __config_util__ will look for an .INI file named __some_script.ini__ and load it.

If no command-line parameter is supplied, and no .INI file with the script's basename is found, then  __config_util__ scans the current directory for all .INI files, presents the list of files to the user, and allows the user to choose one.

## Includes

The primary .INI file may include other .INI files (only one level of nesting is currently supported).  This is useful for specifying default values across a set of .INI files, or for placing authentication parameters in an included .INI file which is in a .gitignore path, etc.

Syntax for includes is:

```ini
[config]
include=other_file.ini
```
Or, if including multiple files:
```ini
[config]
include=file1.ini,file2.ini,file3.ini 
```





