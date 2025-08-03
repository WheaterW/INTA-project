telnet server port
==================

telnet server port

Function
--------



The **telnet server port** command changes the port number that a Telnet server monitors.

The **undo telnet server port** command restores the port number that the Telnet server monitors to the default value.



By default, the Telnet server monitors the port number 23.


Format
------

**telnet server port** *port-number*

**undo telnet server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the monitoring port number of the Telnet server. | The value is 23 or an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A Telnet client can log in successfully with no port specified only when the server is monitoring port 23. If the server is monitoring another port, the port number must be specified upon login.The **telnet server port** command changes the IPv4 and IPv6 port number that a Telnet server monitors.After the monitoring port number is changed, all connections are disconnected and the server starts to monitor new port numbers.

**Precautions**

The Telnet protocol has security risks. You are advised to use the SSH v2 protocol.


Example
-------

# Set the monitoring port number of the Telnet server to 1026.
```
<HUAWEI> system-view
[~HUAWEI] telnet server port 1026

```