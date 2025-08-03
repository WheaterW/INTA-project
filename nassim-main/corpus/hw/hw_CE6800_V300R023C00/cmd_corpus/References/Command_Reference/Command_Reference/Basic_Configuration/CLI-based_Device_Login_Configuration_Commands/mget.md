mget
====

mget

Function
--------



The **mget** command transfers multiple files from the remote server to local device.




Format
------

**mget** *remote-filenames*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-filenames* | Specifies the multiple remote files, which are to be copied to local device.  This parameter contains more than one file name separated by blank space. The file name can contain wild card characters. | Remote file name is a string data type. The string length range is from 1 to 256 characters. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* This command cannot be used to download the entire directory and all files in its subdirectories. To download the entire directory, you can compress the directory into a .tar file for transfer.
* The system prompts a confirmation message to the user before file transfer. You can disable the prompt message using the **undo prompt** command.
* If the file exists in the local device, the system asks the user whether to overwrite the local file.

**Precautions**

The MGET supports downloading a maximum of 1024 files at a time. If the number of files on the server exceeds the upper limit, batch downloading cannot be performed.


Example
-------

# Transfer all files starting with 1 on the FTP server at 10.18.26.141 to the local device.
```
<HUAWEI> ftp 10.18.26.141
Trying 10.18.26.141 ...
Press CTRL + K to abort
Connected to 10.18.26.141.
220 (vsFTPd 2.0.4)
Username:ab
c331 Please specify the password.
Password:230 Login successful.
[ftp] mget /home/1*.txt
mget /home/1mb.txt [transfer file [y/n]]? y
229 Entering Extended Passive Mode (|||27705|)
150 Opening BINARY mode data connection for /home/1mb.txt (1038398 bytes).
100% |*************************************|  1014 KB    7.90 MB/s    00:00 ETA
226 File send OK.
1038398 bytes received in 00:00 (7.88 MB/s)
mget /home/1mb1.txt [transfer file [y/n]]? y
229 Entering Extended Passive Mode (|||47120|)
150 Opening BINARY mode data connection for /home/1mb1.txt (1875968 bytes).
100% |*************************************|  1832 KB   11.26 MB/s    00:00 ETA
226 File send OK.
1875968 bytes received in 00:00 (11.24 MB/s)

```