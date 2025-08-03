sftp max-sessions
=================

sftp max-sessions

Function
--------



The **sftp max-sessions** command configures the maximum number of clients that can be connected to the server at any point of time for SFTP service.

The **undo sftp max-sessions** command restores the default maximum number of clients that can be connected to the SSH server with SFTP service.



By default, the maximum number of clients that can be connected to the SFTP server is 5.


Format
------

**sftp max-sessions** *max-session-count*

**undo sftp max-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-session-count* | Specifies the maximum number of sessions for SFTP. | The value is an integer ranging from 0 to 15. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



You can use this command to configure the maximum number of SFTP clients that can be connected to the server at any point of time for SFTP service, and it takes effect for both IPv4 and IPv6 connections.NOTE:If the configured max-sessions value is less than the number of current connections, then the current connection is not disconnected and the server does not accept any new connection.




Example
-------

# Configure a maximum of 10 sessions for SFTP.
```
<HUAWEI> system-view
[~HUAWEI] sftp max-sessions 10

```