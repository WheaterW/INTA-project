bmp-session alias
=================

bmp-session alias

Function
--------



The **bmp-session alias** command specifies a BMP session address and a session alias for a BMP device to set up a TCP connection with a monitoring server.

The **undo bmp-session alias** command restores the default configuration.



By default, no BMP session address is set for a BMP device. In this case, the client is not in TCP connections with any monitoring servers.


Format
------

**bmp-session** [ **vpn-instance** *vrf-name* ] *ipv4-address* **alias** *alias-name*

**undo bmp-session** [ **vpn-instance** *vrf-name* ] *ipv4-address* **alias** *alias-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vrf-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv4-address* | Specifies the IPv4 address of a BMP session. | The value is in dotted decimal notation. |
| **alias** *alias-name* | Specifies a session alias. When the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify session aliases for differentiation. | The value is a string of 1 to 31 case-sensitive characters. Spaces are allowed only when the string is enclosed in double quotation marks (""). |



Views
-----

BMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status of devices in real time, such as the establishment and termination status of BGP peer relationships and route update status. After a TCP connection is established between a device and a monitoring server, the device reports BGP running status to the monitoring server, improving network monitoring efficiency. To specify a BMP session address for a BMP device to establish a TCP session with a monitoring server, run the bmp-session command. If the command is not run, a BMP device cannot establish TCP connections with any monitoring servers, and therefore its BGP running status cannot be monitored on any servers.



**Precautions**



If a device needs to establish TCP connections with multiple monitoring servers, specify different IP addresses. If the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify one IP address and different session aliases (through the alias-name parameter) for differentiation.




Example
-------

# Set the BMP session address to 10.1.1.1 and session alias to aa.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1 alias aa

```