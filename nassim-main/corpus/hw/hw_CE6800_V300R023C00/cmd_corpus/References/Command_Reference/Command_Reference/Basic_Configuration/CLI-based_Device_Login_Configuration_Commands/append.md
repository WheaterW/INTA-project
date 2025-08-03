append
======

append

Function
--------



The **append** command adds the content of local files to the end of the file on the FTP server.




Format
------

**append** *local-filename* [ *remote-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-filename* | Specifies the local-file name. | Local-filename is a string data type. The string length range is from 1 to 128 characters. |
| *remote-filename* | Specifies the remote-filename. If the remote-file name is not present, the local-filename can be used as remote-filename. The remote-filename depends on the file system of FTP server. | Local-filename is a string data type. The string length range is from 1 to 128 characters. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you have specified the remote-filename and the remote file does not exist, a new remote file is created with the same name as that of the local-filename. The local file data is appended in the newly created file. If you have not specified the remote-filename, the local-filename is used as remote-filename and stored the file in the remote computer.


Example
-------

# Append a local file sample2.txt to the remote file sample1.txt on an FTP server.
```
<HUAWEI> ftp 10.1.1.2
[ftp] append sample2.txt sample1.txt

```

# Append a local file a.txt to the remote file having the same name as that of the local file on an FTP server.
```
<HUAWEI> ftp 10.1.1.2
[ftp] append a.txt

```