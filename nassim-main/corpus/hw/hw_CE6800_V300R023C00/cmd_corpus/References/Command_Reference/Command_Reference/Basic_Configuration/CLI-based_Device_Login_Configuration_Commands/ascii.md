ascii
=====

ascii

Function
--------



The **ascii** command specifies the file transfer data type to ASCII.



By default, the data type is ASCII.


Format
------

**ascii**


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

American Standard Code for Information Interchange (ASCII), a set of 128 symbols that any computer in the world can display.Transferring a binary file in ASCII mode corrupts the binary file structure.

**Prerequisites**

ASCII mode is used for the transfer of ASCII files only. FTP server supports ascii mode for data transmission. But in device, user has to switch to binary mode for data transfer.


Example
-------

# Set the data transmission type to ASCII mode.
```
<HUAWEI> ftp 10.1.1.2
[ftp] ascii

```