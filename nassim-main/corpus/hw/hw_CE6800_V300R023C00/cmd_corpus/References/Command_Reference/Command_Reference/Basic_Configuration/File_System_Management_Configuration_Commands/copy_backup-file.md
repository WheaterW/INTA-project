copy backup-file
================

copy backup-file

Function
--------



The **copy backup-file** command copies files in the backup area to a specified directory.




Format
------

**copy backup-file file-name** *scrFile* **path** *desFile*

**copy backup-file all path** *desFile*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **path** *desFile* | Specifies the name of the destination file or directory to be copied. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |
| **all** | Copies all files from the backup area. | - |
| **file-name** *scrFile* | Specifies the name of the source file to be copied from the backup area. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **copy backup-file** command copies files in the backup area to a specified directory.

**Configuration Impact**

After the command is run, one of the following situations may occur:

* If the destination file name is the same as the name of an existing file, the system prompts you whether to override the existing file. If you choose to override the existing file and the file is write-protected, the file will fail to be overridden.
* If the destination file is a directory, the destination file name is the same as the source file name.

**Precautions**



When coping a file, a user can press Ctrl+C to cancel the operation.




Example
-------

# Copy the example.ini file from the backup area to the flash directory.
```
<HUAWEI> copy backup-file file-name backup:/example.ini path flash:
Info: Are you sure to copy backup:/example.ini to flash:/example.ini? [Y/N]:y
100%  complete
Info: Copying file backup:/example.ini to flash:/example.ini...Done.

```

# Copy all files in the backup area to the flash directory.
```
<HUAWEI> copy backup-file all path flash:
Info: Are you sure to copy backup:/persisSafeMedia.txt to flash:/persisSafeMedia.txt? [Yes/No/Cancel]:yes
Info: The file flash:/persisSafeMedia.txt already exists. Are you sure to overwrite it? [Yes/No/Cancel]:y
100%  complete
Info: Copying file backup:/persisSafeMedia.txt to flash:/persisSafeMedia.txt...Done.
Info: Are you sure to copy backup:/persisSafeMediaEx.txt to flash:/persisSafeMediaEx.txt? [Yes/No/Cancel]:y
Info: The file flash:/persisSafeMediaEx.txt already exists. Are you sure to overwrite it? [Yes/No/Cancel]:y
100%  complete
Info: Copying file backup:/persisSafeMediaEx.txt to flash:/persisSafeMediaEx.txt...Done.
Info: Are you sure to copy backup:/persisSafeMediaR5C10.txt to flash:/persisSafeMediaR5C10.txt? [Yes/No/Cancel]:y
Info: The file flash:/persisSafeMediaR5C10.txt already exists. Are you sure to overwrite it? [Yes/No/Cancel]:y
100%  complete
Info: Copying file backup:/persisSafeMediaR5C10.txt to flash:/persisSafeMediaR5C10.txt...Done.
Info: Are you sure to copy backup:/snmpsystemruninfo.bin to flash:/snmpsystemruninfo.bin? [Yes/No/Cancel]:y
Info: The file flash:/snmpsystemruninfo.bin already exists. Are you sure to overwrite it? [Yes/No/Cancel]:y
100%  complete
Info: Copying file backup:/snmpsystemruninfo.bin to flash:/snmpsystemruninfo.bin...Done.
Info: Are you sure to copy backup:/vrpfile.ini to flash:/vrpfile.ini? [Yes/No/Cancel]:y
Info: The file flash:/vrpfile.ini already exists. Are you sure to overwrite it? [Yes/No/Cancel]:y
100%  complete
Info: Copying file backup:/vrpfile.ini to flash:/vrpfile.ini...Done.
Error: flash:/V300R020C10SPC100-0224172444.cc is protected.
Error: flash:/device.sys is protected.
Error: flash:/vrpcfg.zip is protected.

```