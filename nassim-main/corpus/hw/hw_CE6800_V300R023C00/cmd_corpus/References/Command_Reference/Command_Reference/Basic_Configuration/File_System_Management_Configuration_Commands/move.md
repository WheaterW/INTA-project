move
====

move

Function
--------



The **move** command moves a file within a device.




Format
------

**move** *source-filename* *destination-filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-filename* | Specifies the name of the source file. | The wildcard "\*" cannot be used. The value is a character string in the format of [ <drive> ][ path ] [ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive>[ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |
| *destination-filename* | Specifies the name of the destination file or directory. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **move** command to change the path of the current file.

**Configuration Impact**

The name of the destination file can be a directory name. In this case, the **move** command moves the source file with the name unchanged to the directory.If the destination file name is the same as the name of an existing directory, moving a file fails. If the destination file name is the same as the name of an existing file, the system prompts you whether to override the existing file.


Example
-------

# Move the file sample.txt from flash:/test/.
```
<HUAWEI> move flash:/test/sample.txt flash:/test.txt
Warning: Move file flash:/test/sample.txt to flash:/test.txt? [Y/N]:y
100%  complete  
Info: Move file flash:/test/sample.txt to flash:/test.txt...Done.

```