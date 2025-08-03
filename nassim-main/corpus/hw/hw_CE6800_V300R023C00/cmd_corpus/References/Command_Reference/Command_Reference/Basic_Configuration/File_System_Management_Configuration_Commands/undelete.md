undelete
========

undelete

Function
--------



The **undelete** command restores a dumped file.




Format
------

**undelete** *filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filename* | Specifies the name of a file to be restored. | The wildcard "\*" can be used. The value is a character string in the format of [ <drive> ][ path ] [ file-name ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ file-name ], and a relative path is in the format of [ path ][ file-name ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **undelete** command to restore the file that is incorrectly dumped. If the parameter /unreserved is configured in the delete command, the file cannot be restored.

**Prerequisites**

The file to be restored is saved in the recycle bin.

**Configuration Impact**

If the file to be restored has the same name as an existing directory, the operation fails. If the file to be restored has the same name as an existing file, the system prompts you whether to overwrite the existing file.


Example
-------

# Restore the dumped file sample.bak.
```
<HUAWEI> undelete flash:/sample.bak
Info: Are you sure to undelete flash:/sample.bak ?[Y/N] : y
Info: Undeleting file flash:/sample.bak...Done.

```