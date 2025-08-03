reset recycle-bin
=================

reset recycle-bin

Function
--------



The **reset recycle-bin** command permanently deletes files in the recycle bin.




Format
------

**reset recycle-bin**

**reset recycle-bin /f**

**reset recycle-bin** *filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **/f** | Deletes all files from the recycle bin without displaying a message for confirmation. | - |
| *filename* | Specifies the name of a file to be deleted. | The wildcard "\*" can be used. The value is a character string in the format of [ <drive> ][ path ] [ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **delete** command to dump a file to the recycle bin. To delete the file permanently, you can run the **reset recycle-bin** command.

**Configuration Impact**

The **reset recycle-bin** command permanently deletes a specified file, and the file cannot be restored. The **reset recycle-bin** command clears the recycle bin, where all files cannot be restored.


Example
-------

# Delete all files from the recycle bin.
```
<HUAWEI> reset recycle-bin /f
Info: Are you sure to clear all file in recycle bin? [Y/N]:y
Info: Clearing all file in recycle bin...Done.

```