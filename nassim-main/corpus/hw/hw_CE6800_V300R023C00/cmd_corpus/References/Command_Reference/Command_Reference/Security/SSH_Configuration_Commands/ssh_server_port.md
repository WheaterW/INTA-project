ssh server port
===============

ssh server port

Function
--------



The **ssh server port** command changes the port number that an SSH server monitors.

The **undo ssh server port** command restores the port number that the SSH server monitors to the default value.



By default, the SSH server monitors the port number 22.


Format
------

**ssh server port** *port-number*

**undo ssh server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the port number that an SSH server monitors. | The value can be 22 or is an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An SSH client can log in successfully with no port specified only when the server is monitoring port 22. If the server is monitoring another port, the port number must be specified upon login.The **ssh server port** command changes the IPv4/IPv6 port number that an SSH server monitors.After the monitoring port number is changed, all connections are disconnected and the server starts to monitor new port numbers.


Example
-------

# Set the monitoring port number of the SSH server to 1025.
```
<HUAWEI> system-view
[~HUAWEI] ssh server port 1025

```