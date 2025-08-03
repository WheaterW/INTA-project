telnet ipv6 server port
=======================

telnet ipv6 server port

Function
--------



The **telnet ipv6 server port** command changes the IPv6 port number that a Telnet server monitors.

The **undo telnet ipv6 server port** command restores the IPv6 port number that the Telnet server monitors to the default value.



By default, the Telnet server ipv6 monitors the port number 23.


Format
------

**telnet ipv6 server port** *port-number*

**undo telnet ipv6 server port**


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

A Telnet client can log in successfully with no port specified only when the server is monitoring port 23. If the server is monitoring another port, the port number must be specified upon login.After the monitoring port number is changed, all connections are disconnected and the server starts to monitor new port numbers.


Example
-------

# Set the IPv6 port number that the Telnet server monitors to 1025.
```
<HUAWEI> system-view
[~HUAWEI] telnet ipv6 server port 1025

```