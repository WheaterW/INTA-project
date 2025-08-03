ops install file
================

ops install file

Function
--------



The **ops install file** command installs a single file.

The **ops uninstall file** command removes a single file or directory.




Format
------

**ops install file** *scrFile* [ **destination** *directory* ]

**ops uninstall file** *file-name-or-dir*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *scrFile* | Specifies the name of the file to be installed. | The value is a string of 1 to 127 characters without spaces. The value can contain the path and wildcards. The restriction is that the sum of the path length and the file name length is not greater than 127, and the installation path includes $\_user.  When quotation marks are used around the string, spaces are allowed in the string. |
| **destination** *directory* | Specifies the installation path of the file. | The value does not contain a drive letter. In the case of an absolute path, the root directory must be $\_user. In the case of a relative path, the $\_user directory is used by default. If the specified directory does not exist, a new directory is created. A maximum of seven levels of subdirectories can be created under $\_user. The value is a string of 1 to 127 characters. The restriction is that the sum of the path length and the file name length is not greater than 127, and the installation path includes $\_user. |
| *file-name-or-dir* | Specifies the name of the file or directory to be removed. | The value is a string of 1 to 127 characters. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To install a file in a directory in a specified destination, run the **ops install file** command. If this parameter is not specified, the file is installed in the default directory $\_user.The **dir** command can be run to display information about files that are installed in the $\_user directory.To remove a file or files in a directory, run the ops uninstall file command.

* If a file is specified in the command, the file will be deleted.
* If a directory is specified in the command, all files in the directory and its sub-directory will be deleted.
* If the file to be deleted is associated with a maintenance assistant, the delete operation is stopped.
* The asterisk (\*) is supported in the command.
* If \* or \*/ is specified in the command, all files in the $\_user directory will be deleted.
* If a folder /\* is specified in the command, all files in the folder will be deleted.
* If \*.py is specified in the command, all Python files in the $\_user directory will be deleted.

**Precautions**

* Only installed files can be executed.
* If a specified destination directory does not exist, a new one is created. A maximum of seven sub-directories can be created in the $\_user directory.
* Users can copy files to the $\_user directory only using the **ops install file** command. Files in the $\_user directory will be automatically backed up to the slave main control board.
* The installed files can be re-installed only after being deleted using the ops uninstall file command.
* Installing files less than 100 MB in the $\_user directory is recommended. Otherwise, the synchronization between the master and slave main control boards will be affected.
* The ops uninstall file command does not remove the script associated with a maintenance assistant. The script can be deleted only after being disassociated from the maintenance assistant.
* The other scripts used by the script associated with a maintenance assistant are not protected and can be removed. Therefore, implementing associated functions in a script is recommended.


Example
-------

# Remove the file config.py.
```
<HUAWEI> ops uninstall file config.py

```

# Install the file config.py in the default directory.
```
<HUAWEI> ops install file config.py

```