dir (FTP client view)
=====================

dir (FTP client view)

Function
--------



The **dir** command displays information about all files in the specified directory on the FTP server.



By default, the details about the current directory are displayed


Format
------

**dir** [ *remote-directory* [ *local-filename* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-directory* | Specifies the remote directory name. | The value is a string of 1 to 128 case-sensitive characters without a blank space. |
| *local-filename* | Specifies the saved local file name. | The value is a string of 1 to 128 case-sensitive characters without a blank space. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to display files in the specified directory on the FTP server. To save the file content in the local file, you need to specify local-filename.

**Precautions**



The flash has internal partitions. The remaining space information shown in the dir flash: command output greatly differs from that shown in the dir flash:/logfile/ command output. Before you install the target system software, run the dir flash: command to verify whether the remaining space is sufficient.




Example
-------

# Query the directory names.
```
<HUAWEI> ftp 1.1.1.1
[ftp] dir

```

# Query the directories of FTP server named as new\_folder.
```
<HUAWEI> ftp 1.1.1.1
[ftp] dir new_folder

```

# Query the new\_folder and save the query result in the file output.txt.
```
<HUAWEI> ftp 1.1.1.1
[ftp] dir new_folder output.txt

```