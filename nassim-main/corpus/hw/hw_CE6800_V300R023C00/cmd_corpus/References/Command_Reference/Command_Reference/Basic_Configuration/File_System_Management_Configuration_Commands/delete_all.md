delete all
==========

delete all

Function
--------



The **delete all** command deletes all the specified files from the user directory of the device.




Format
------

**delete** *filename* **all**

**delete /unreserved** *filename* **all**

**delete /quiet** *filename* **all**

**delete /unreserved /quiet** *filename* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filename* | Specifies the name of a file to be dumped. | The value is a character string in the format of [ <drive> ][ <path> ][ <file-name> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ][ <file-name> ], and a relative <path> is in the format of [ <path> ][ <file-name> ]. That is, a relative <path> is the root <path> of the current working <path>. |
| **/unreserved** | Deletes a specified file thoroughly. The deleted file cannot be restored. | - |
| **/quiet** | Delete without confirm. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Dumping a file implies placing the file in the recycle bin. The **dir** command does not display information about dumped files. The dir /all command displays information about all files, including dumped files in the recycle bin.

**Configuration Impact**

* You can run the **undelete** command to restore a file that is dumped through this command without the parameter /unreserved. To delete the file from the recycle bin, you can run the **reset recycle-bin** command.
* If two files with the same name are dumped from two directories, both files are saved in the recycle bin and can be restored separately.
* If a file to be dumped is under protection, such as the .cc file, dumping the file causes the system to prompt a message.

**Precautions**

* If you run this command without the /unreserved parameter to delete a file when the recycle bin space is insufficient, a message is displayed indicating a deletion failure. In this case, run the **reset recycle-bin** command to clear the recycle bin before deleting the file.
* If the disk space is still insufficient after you clear the recycle bin, run the delete /unreserved command to delete the file permanently. The file cannot be restored after being deleted.
* After the system is restarted, if a failure message is displayed when you delete a software package or configuration file before service processes become stable, perform the deletion only when the processes become stable.


Example
-------

# Dump the file test.txt.
```
<HUAWEI> delete flash:/test.txt all
Info: Are you sure to delete flash:/test.txt? [Yes/All/No/Cancel]:y
Info: Deleting file flash:/test.txt...Done.

```