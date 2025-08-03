ftp server ip-max-sessions
==========================

ftp server ip-max-sessions

Function
--------



The **ftp server ip-max-sessions** command configures the maximum number of clients that can be connected from a single IP to the server at any point of time for FTP service.

The **undo ftp server ip-max-sessions** command restores the default maximum number of clients that can be connected from a single IP to the server aty any point of time for FTP service.



By default, the maximum number of clients that can be connected from a single IP to the FTP server is 15.


Format
------

**ftp server ip-max-sessions** *ip-max-sessions-num*

**undo ftp server ip-max-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-max-sessions-num* | Set the maximum number of FTP connections to the server for a single IP address. | The value is an integer that ranges from 1 to 15. The default value is 15. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to configure the maximum number of FTP clients that can be connected from a single IP to the server at any point of time for FTP service, and it takes effect for both IPv4 and IPv6 connections. If the configured max-sessions value is less than or equal to the number of current connections, then the current connection is not disconnected and the server does not accept any new connection.


Example
-------

# Configure maximum of 10 sessions from a single IP for ftp.
```
<HUAWEI> system-view
[~HUAWEI] ftp server ip-max-sessions 10

```