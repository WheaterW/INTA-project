route-mode local-rib (BMP monitor view)
=======================================

route-mode local-rib (BMP monitor view)

Function
--------



The **route-mode local-rib** command enables a device to send statistics about Local-RIB (Routing Information Base) best routes in a specified BGP address family to a monitoring server.

The **undo route-mode local-rib** command restores the default configuration.



By default, a BMP device is not enabled to report any routing information to any server.


Format
------

**route-mode** { **ipv4-family** | **ipv6-family** } **unicast** **local-rib** [ **add-path** | **all** ] [ **path-marking** ]

**undo route-mode** { **ipv4-family** | **ipv6-family** } **unicast** **local-rib** [ **add-path** | **all** ] [ **path-marking** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4-family** | Configures the device to send statistics about Local-RIB routes of BGP peers in the IPv4 address family to the monitoring server. | - |
| **ipv6-family** | Configures the device to send statistics about Local-RIB routes of BGP peers in the IPv6 address family to the monitoring server. | - |
| **unicast** | Configures the device to send statistics about Local-RIB routes of BGP peers in the unicast address family to the monitoring server. | - |
| **add-path** | Configures the device to send statistics about Add-Path routes of BGP peers to the monitoring server. If the parameter is specified, statistics about load balancing routes are reported to the monitoring server. | - |
| **all** | Configures the device to report all routes. | - |
| **path-marking** | Configures the device to report path status. | - |



Views
-----

BMP monitor view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure the device to send statistics about Local-RIB routes (routes received from peers and locally imported routes) of BGP peers in a specified address family to the monitoring server, run the route-mode local-rib command.



**Prerequisites**

The BMP-Monitor view has been displayed using either of the following commands:

* monitor public: The BMP device sends statistics about Local-RIB routes of all BGP peers in the public network address family to the monitoring server.
* monitor vpn-instance: The BMP device sends statistics about Local-RIB routes of all BGP peers in a specified VPN instance address family to the monitoring server.


Example
-------

# Configure the BMP device to send statistics about the Local-RIB routes of all BGP peers in the IPv4 unicast address family to the monitoring server.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] monitor public
[*HUAWEI-bmp-session-10.1.1.1-public] route-mode ipv4-family unicast local-rib

```