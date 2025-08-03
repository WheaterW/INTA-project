monitor peer
============

monitor peer

Function
--------



The **monitor peer** command displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in the public network address family to be monitored.

The **undo monitor peer** command restores the default configuration.



By default, the BGP running status of BGP peers is not monitored.


Format
------

**monitor peer** *ipv4-address*

**monitor peer** *ipv6-address*

**undo monitor peer** *ipv4-address*

**undo monitor peer** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status of devices in real time, such as the establishment and termination status of BGP peer relationships and route update status. To allow the BGP running status of a specified BGP peer in the public network address family to be monitored, run the monitor peer command. After a TCP connection is established between the device and the monitoring server, the device reports BGP running status to the monitoring server, improving network monitoring efficiency.



**Follow-up Procedure**

Perform either of the following operations as required:

* Run the route-mode { { { ipv4-family | ipv6-family } unicast } | ipv4-family vpnv4 | ipv6-family vpnv6 } adj-rib-in { pre-policy | post-policy } command to set the type of RIB-in route (received from a specified peer in a specified public network address family) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { { ipv4-family | ipv6-family } unicast } | ipv4-family vpnv4 | ipv6-family vpnv6 } adj-rib-out { pre-policy | post-policy } command to set the type of RIB-out route (to be advertised or already advertised to a specified peer in a specified public network address family) whose statistics are to be sent by the device to the monitoring server.

**Precautions**



This command cannot be used to monitor a specified peer in a distributed instance.




Example
-------

# Display the BMP-Monitor view and allow the BGP running status of a specified BGP peer in the public network address family to be monitored.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1 alias a
[*HUAWEI-bmp-session-10.1.1.1-a] monitor peer 10.1.1.1

```