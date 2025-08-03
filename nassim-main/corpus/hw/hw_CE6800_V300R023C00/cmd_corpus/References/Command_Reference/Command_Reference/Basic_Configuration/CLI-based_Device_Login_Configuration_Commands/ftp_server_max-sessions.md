ftp server max-sessions
=======================

ftp server max-sessions

Function
--------



The **ftp server max-sessions** command configures the maximum number of clients that can be connected to the server at any point of time for FTP service.

The **undo ftp server max-sessions** command restores the default maximum number of clients that can be connected to the server aty any point of time for FTP service.



By default, the maximum number of clients that can be connected to the FTP server is 15.


Format
------

**ftp server max-sessions** *max-session-count*

**undo ftp server max-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-session-count* | Specify the maximum number of sessions for FTP. | The value is an integer that ranges from 0 to 15. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to configure the maximum number of FTP clients that can be connected to the server at any point of time for FTP service, and it takes effect for both IPv4 and IPv6 connections. If the configured max-sessions value is less than or equal to the number of current connections, then the current connection is not disconnected and the server does not accept any new connection.


Example
-------

# Configure maximum of 10 sessions for ftp.
```
<HUAWEI> system-view
[~HUAWEI] ftp server max-sessions 10

```