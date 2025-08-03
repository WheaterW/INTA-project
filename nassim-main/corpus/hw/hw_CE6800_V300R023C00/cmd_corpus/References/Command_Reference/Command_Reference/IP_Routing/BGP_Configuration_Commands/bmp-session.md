bmp-session
===========

bmp-session

Function
--------



The **bmp-session** command specifies a BMP session address for a BMP device to set up a TCP connection with a monitoring server.

The **undo bmp-session** command restores the default configuration.



By default, no BMP session address is set for a BMP device. In this case, the client is not in TCP connections with any monitoring servers.


Format
------

**bmp-session** [ **vpn-instance** *vrf-name* ] *ipv4-address*

**undo bmp-session** [ **vpn-instance** *vrf-name* ] *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vrf-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv4-address* | Specifies the IPv4 address of a BMP session. | The value is in dotted decimal notation. |



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



A BMP device can be connected to multiple monitoring servers. You can specify different IP addresses or the same IP address but different port numbers (by specifying the alias-name parameter) to identify the monitoring servers. When a BMP device is connected to multiple monitoring servers, the BMP sends data to multiple monitoring servers at the same time.




Example
-------

# Set the BMP session address to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1

```