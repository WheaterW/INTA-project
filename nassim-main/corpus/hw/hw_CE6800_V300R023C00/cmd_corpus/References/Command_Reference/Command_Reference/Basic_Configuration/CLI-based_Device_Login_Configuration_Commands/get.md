get
===

get

Function
--------



The **get** command copies a file from the FTP server to local device.




Format
------

**get** *remote-filename* [ *local-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-filename* | Specifies the remote file which is to be copied to local file. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| *local-filename* | Specifies the name of the local file copied from the FTP server. If the local file name does not exist, the file name on the FTP server is used. | Remote-filename is a string data type. The string length range is from 1 to 128 characters. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the local file name is not specified, the downloaded file is saved using the same name as that of the remote file in the FTP server.


Example
-------

# In binary mode, copy a remote file to a local directory to overwrite an existing file.
```
<HUAWEI> ftp 10.1.1.1
[ftp] get XXX_remote.cc XXX_local.cc
Warning: The file dd.cc already exists. Overwrite it? [Y/N]:y
200 Port command okay. 
150 Opening BINARY mode data connection for /XXX_remote.cc. 
| 100% [***********]  
226 Transfer complete.  

FTP: 8884664 byte(s) received in 10.356 second(s) 651.171Kbyte(s)/sec.

```

# In ASCII mode, copy a remote file to a local directory and change the local file name to R.txt.
```
<HUAWEI> ftp 10.1.1.1
[ftp] get wrong.log R.txt
Warning: The file may not transfer correctly in ASCII mode.
213 5554664 
200 Port command okay. 
150 Opening ASCII mode data connection for /wrong.log. 
| 100% [***********]  
226 Transfer complete.  

FTP: 5554664 byte(s) received in 8.356 second(s) 649.171Kbyte(s)/sec.

```