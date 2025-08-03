rename (User view)
==================

rename (User view)

Function
--------



The **rename** command renames a file or a directory.




Format
------

**rename** *source-filename* *destination-filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-filename* | Specifies the name of the source file. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |
| *destination-filename* | Specifies the name of the destination file. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After renaming, the original file name becomes invalid. This command returns error, if a file exists with the new-name.You can run the **rename** command to change the name of a file or a directory.

**Configuration Impact**

If the destination file name is the same as the name of an existing directory or an existing file, the system prompts an error message.If an absolute path is used, the source and destination paths must be the same.


Example
-------

# Rename the file sample.txt as sample.bak.
```
<HUAWEI> rename test.txt test1.txt
Info: Are you sure to rename file flash:/test.txt to flash:/test1.txt? [Y/N]:y
Info: Renaming file flash:/test.txt to flash:/test1.txt...Done.

```