ftp server port
===============

ftp server port

Function
--------



The **ftp server port** command sets the FTP server IPv4 listening port.

The **undo ftp server port** command resets the FTP server IPv4 listening port to default value.



By default, the FTP server IPv4 listening port is 21.


Format
------

**ftp server port** *port-number*

**undo ftp server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the listening port number of the FTP service. | Port number is an integer that is 21 or ranges from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the listening port number of an FTP server is 21. You can directly log in to the device without specifying the port number. Attackers may access the default listening port, consuming bandwidth, deteriorating server performance, and causing authorized users unable to access the server. To improve security, run this command to change the listening port number of the FTP server. After that, attackers are deprived of information about the newly configured listening port number, and the FTP server is thus well protected.The command ftp server port sets the FTP server listening port.

**Configuration Impact**

The FTP server closes all FTP connection and uses the new listening port.If the listening port number of the FTP server is 21, the FTP client can log in to the FTP server without specifying the port number. If the listening port number of the FTP server is not 21, the FTP client needs to specify the port number when trying to log in to the FTP server. The specified port number must be identical with the listening port number of the FTP server.

**Precautions**

The FTP protocol has security risks. You are advised to use the SFTP protocol.


Example
-------

# Set the FTP server listening port as 9000.
```
<HUAWEI> system-view
[~HUAWEI] ftp server port 9000
Warning: This operation will cause all the online Ftp users to be offline. Continue? [Y/N]:y
Warning: Succeeded in changing the listening port of the Ftp server.

```