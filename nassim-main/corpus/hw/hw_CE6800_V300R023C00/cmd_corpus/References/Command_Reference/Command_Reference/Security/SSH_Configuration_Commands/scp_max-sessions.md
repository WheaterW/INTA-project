scp max-sessions
================

scp max-sessions

Function
--------



The **scp max-sessions** command configures the maximum number of SCP clients that can be connected to the SSH server.

The **undo scp max-sessions** command restores the default value.



By default, a maximum of two SCP clients can be connected to the SSH server.


Format
------

**scp max-sessions** *max-session-count*

**undo scp max-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-session-count* | Specify the maximum number of SCP clients that can be connected to the SSH server. | The value is an integer ranging from 0 to 5. The default value is 2. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To configure the maximum number of SCP clients that can be connected to the SSH server, run the scp max-sessions command.If the value specified by the max-session-count parameter is less than the number of current connections, the current connections are not ended but the server no longer accepts any new connections.This command takes effect for both IPv4 and IPv6 connections.




Example
-------

# Set the maximum number of SCP clients that can be connected to the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] scp max-sessions 5

```