verbose
=======

verbose

Function
--------



The **verbose** command enables the verbose mode for FTP.

The **undo verbose** command disables the verbose mode for FTP.



By default, the verbose mode is enabled.


Format
------

**verbose**

**undo verbose**


Parameters
----------

None

Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When you use the verbose command, all FTP response is displayed. After the file is transmitted, it displays the statistics of transmission rate.


Example
-------

# Enable the verbose mode.
```
<HUAWEI> ftp 10.18.26.133
[ftp] verbose
[ftp] get sample.txt
200 PORT command successful
150-Connecting to port 14913150 259.0 kbytes to download
226-File successfully transferred
226 0.366 seconds (measured here), 0.69 Mbytes per second
[ftp] put sample.txt
200 PORT command successful
150 Connecting to port 12289226 File successfully transferred
350 RNFR accepted - file exists, ready for destination
250 File successfully renamed or moved
100% [***********]
[ftp] undo verbose
[ftp] put sample.txt
100% [***********]

```