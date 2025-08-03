telnet server ip-limit-session
==============================

telnet server ip-limit-session

Function
--------



The **telnet server ip-limit-session** command sets the maximum number of Telnet connections to the server for a single IP address.

The undo telnet server ip-limit-session command restores the default maximum number of Telnet connections to the server for a single IP address.



The default maximum number of clients is 64.


Format
------

**telnet server ip-limit-session** *limit-session-num*

**undo telnet server ip-limit-session**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-session-num* | Set the maximum number of Telnet connections to the server for a single IP address. | The value is an integer that ranges from 1 to 64. The default value is 64. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Run this command to set the maximum number of Telnet connections to the server using a single IP address. This prevents login failures caused by a single IP address maliciously occupying the number of connections to the server.


Example
-------

# Set the maximum number of Telnet connections to the server for a single IP address to 22.
```
<HUAWEI> system-view
[~HUAWEI] telnet server ip-limit-session 22

```