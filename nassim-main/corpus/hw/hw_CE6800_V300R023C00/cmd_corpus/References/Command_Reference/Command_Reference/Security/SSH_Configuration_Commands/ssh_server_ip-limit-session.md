ssh server ip-limit-session
===========================

ssh server ip-limit-session

Function
--------



The **ssh server ip-limit-session** command sets the maximum number of connections that a single IP address can connect to the SSH server.

The **undo ssh server ip-limit-session** command restores the maximum number of connections to the SSH server from a single IP address to the default value.



By default, a maximum of 256 connections can be established on the SSH server using a single IP address.


Format
------

**ssh server ip-limit-session** *limit-session-num*

**undo ssh server ip-limit-session**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-session-num* | Sets the maximum number of connections supported by a single IP address. | The value is an integer that ranges from 1 to 256. The default value is 256. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Run this command to set the maximum number of SSH connections for a single IP address, run the ssh-server command, prevents malicious attacks from a single IP occupying the number of connections to the server, causing failure of other IP addresses to connect to the server.


Example
-------

# Set the maximum number of SSH connections for a single IP address to 20.
```
<HUAWEI> system-view
[~HUAWEI] ssh server ip-limit-session 20

```