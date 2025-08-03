ftp ipv6 server port
====================

ftp ipv6 server port

Function
--------



The **ftp ipv6 server port** command sets the FTP server ipv6 listen port.

The **undo ftp ipv6 server port** command resets the FTP server ipv6 listen port to default value.



By default, FTP server ipv6 listen port is 21.


Format
------

**ftp ipv6 server port** *port-number*

**undo ftp ipv6 server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the FTP server ipv6 listen port. | Port number is an integer that is 21 or ranges from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the listening port number of an FTP server is 21. You can directly log in to the device without specifying the port number. Attackers may access the default listening port, consuming bandwidth, deteriorating server performance, and causing authorized users unable to access the server. To improve security, run this command to change the listening port number of the FTP server. After that, attackers are deprived of information about the newly configured listening port number, and the FTP server is thus well protected.

**Configuration Impact**

The FTP server closes all FTP connection and uses the new listening port.If the listening port number of the FTP server is 21, the FTP client can log in to the FTP server without specifying the port number. If the listening port number of the FTP server is not 21, the FTP client needs to specify the port number when trying to log in to the FTP server. The specified port number must be identical with the listening port number of the FTP server.


Example
-------

# Set the FTP server listen port as 9000.
```
<HUAWEI> system-view
[~HUAWEI] ftp ipv6 server port 9000
Warning: This operation will cause all the online Ftp users to be offline. Continue? [Y/N]:y
Warning: Succeeded in changing the listening port of the Ftp server.

```