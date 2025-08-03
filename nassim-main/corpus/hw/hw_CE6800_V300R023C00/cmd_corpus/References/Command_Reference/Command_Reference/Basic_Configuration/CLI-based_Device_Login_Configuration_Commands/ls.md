ls
==

ls

Function
--------



The **ls** command lists all the directories and files in the present working directory of remote machine.




Format
------

**ls** [ *remote-directory* [ *local-filename* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-directory* | Specifies the directory name in the remote machine. | Remote directory name is a string data type. The string length range is from 1 to 128 characters. |
| *local-filename* | Specifies the local file to be saved in the directory of remote machine. | Local file name is a string data type. The string length range is from 1 to 128 characters. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the ls command displays all the files, if you do not specify any parameters.


Example
-------

# List the directories and files.
```
<HUAWEI> ftp 10.18.26.133
[ftp] ls

```

# List the directories of remote directory new\_folder.
```
<HUAWEI> ftp 10.18.26.133
[ftp] ls new_folder

```

# List the directories and files of new\_folder and to place in a local file output.txt.
```
<HUAWEI> ftp 10.18.26.133
[ftp] ls new_folder output.txt

```