mput
====

mput

Function
--------



The **mput** command transfers multiple files from the local device to remote server.




Format
------

**mput** *local-filenames*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-filenames* | Specifies multiple files, which are to be copied from the local device to the remote server.  This parameter contains multiple file names separated by blank spaces. The file name can contain wild card characters. | Local file name is a string data type. The string length range is from 1 to 256 characters. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command cannot be used to upload the entire directory and all files in its subdirectories. To upload the entire directory, you can compress the directory into a .tar file for transfer.

The system prompts a confirmation message to the user before file transfer. You can disable the prompt message using the **undo prompt** command.


Example
-------

# Transfer two local files to a remote server.
```
<HUAWEI> ftp 1.1.1.1
Trying 1.1.1.1
Press CTRL + K to abort
Connected to 1.1.1.1
220 (vsFTPd 2.2.1)
Username:root
331 Please specify the password.
Password:
230 Login successful.
[ftp] mput 1*.txt 2*.txt 3*.txt
Warning: Continue to upload 1.txt?Please select [Y/N]:y
200 EPRT command successful. Consider using EPSV.
150 Ok to send data.
226 File receive OK.
\     100% [***********]
FTP: 12386115 byte(s) send in 2.431549000 second(s) 4975.654Kbyte(s)/sec.
Warning: Continue to upload 2.txt?Please select [Y/N]:y
200 EPRT command successful. Consider using EPSV.
150 Ok to send data.
226 File receive OK.
/     100% [***********]
FTP: 12386115 byte(s) send in 3.1769665647 second(s) 3808.505Kbyte(s)/sec.
Warning: Continue to upload 3.txt?Please select [Y/N]:y
200 EPRT command successful. Consider using EPSV.
150 Ok to send data.
226 File receive OK.
|     100% [***********]
FTP: 12386115 byte(s) send in 3.1636597647 second(s) 3824.159Kbyte(s)/sec.

```