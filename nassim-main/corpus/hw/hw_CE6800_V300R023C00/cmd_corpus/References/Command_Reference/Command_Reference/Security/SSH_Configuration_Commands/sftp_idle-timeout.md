sftp idle-timeout
=================

sftp idle-timeout

Function
--------



The **sftp idle-timeout** command sets the timeout period for an SFTP client to suspend connection from the SSH server.

The **undo sftp idle-timeout** command restores the default timeout period.



By default, the timeout period is 10 minutes.


Format
------

**sftp idle-timeout** *minutes* [ *seconds* ]

**undo sftp idle-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minutes* | Specifies the time period in minutes. | It is an integer data type. The value range is from 0 to 35791 minutes. |
| *seconds* | Specifies the time period in seconds. | It is an integer data type. The value range is from 0 to 59 seconds. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The sftp idle-timeout command is used to set the timeout period to suspend the connection if you do not execute any command for a certain period of time.You can disable the timeout disconnection function by running the **sftp idle-timeout 0 0** command.This command takes effect for both IPv4 and IPv6 connections.




Example
-------

# Set the timeout period to 1 minute and 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] sftp idle-timeout 1 30

```