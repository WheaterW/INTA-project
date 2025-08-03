monitor vpn-instance peer
=========================

monitor vpn-instance peer

Function
--------



The **monitor vpn-instance peer** command displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in a specified VPN instance address family to be monitored.

The **undo monitor vpn-instance peer** command restores the default configuration.



By default, the BGP running status of BGP peers is not monitored.


Format
------

**monitor vpn-instance** *vpn-instance-name* **peer** *ipv4-address*

**monitor vpn-instance** *vpn-instance-name* **peer** *ipv6-address*

**undo monitor vpn-instance** *vpn-instance-name* **peer** *ipv4-address*

**undo monitor vpn-instance** *vpn-instance-name* **peer** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status of devices in real time, such as the establishment and termination status of BGP peer relationships and route update status. To allow the BGP running status of a specified BGP peer in a specified VPN instance address family to be monitored, run the monitor vpn-instance peer command. After a TCP connection is established between the device and the monitoring server, the device reports BGP running status to the monitoring server, improving network monitoring efficiency.



**Follow-up Procedure**

Perform either of the following operations as required:

* Run the route-mode { { ipv4-family | ipv6-family } unicast } adj-rib-in { pre-policy | post-policy } command to set the type of RIB-in route (received from a specified peer in a specified VPN instance address family) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { ipv4-family | ipv6-family } unicast } adj-rib-out { pre-policy | post-policy } command to set the type of RIB-out route (to be advertised or already advertised to a specified peer in a specified VPN instance address family) whose statistics are to be sent by the device to the monitoring server.


Example
-------

# Display the BMP-Monitor view and allow the BGP running status of a specified BGP peer in a specified VPN instance address family to be monitored.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1 alias a
[*HUAWEI-bmp-session-10.1.1.1-a] monitor vpn-instance vpn1 peer 10.1.1.1

```