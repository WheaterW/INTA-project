copy (User view)
================

copy (User view)

Function
--------



The **copy** command copies a file.




Format
------

**copy** *source-filename* *destination-filename* [ **all** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-filename* | Specifies the source file name. | The value is a string of case-sensitive characters in the format of [<drive>][path][file name]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |
| *destination-filename* | Specifies the name of the destination file or directory. | The value is a string of case-sensitive characters in the format of [<drive>][path][file name]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |
| **all** | Copy the file to all slots. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the copy command to back up important data.

**Configuration Impact**

After the copy command is run, one of the following situations may occur:

* If the destination file name is the same as the name of an existing file, the system prompts you whether to override the existing file.
* If the name of the destination file is a directory name, the destination file name is the same as the source file name.

**Precautions**



You can press CTRL\_C to stop copying files.A file larger than 2 GB cannot be copied. You are advised to use SFTP to transfer such a file.




Example
-------

# Copy the file sample.txt from flash:/ to flash:/test.txt.
```
<HUAWEI> copy sample.txt test.txt
Info: Are you sure to copy flash:/sample.txt to flash:/test.txt? [Y/N]:y
100%  complete
Info: Copying file flash:/sample.txt to flash:/test.txt...Done.

```