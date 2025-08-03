routing-table limit (VPN instance IPv4 address family view)
===========================================================

routing-table limit (VPN instance IPv4 address family view)

Function
--------



The **routing-table limit** command sets a limit on the maximum number of routes that the IPv4 or IPv6 address family of a VPN instance can support.

The **undo routing-table limit** command restores the default configurations.



By default, there is no limit on the maximum number of routes that the IPv4 or IPv6 address family of a VPN instance can support, but the total number of private network and public network routes on a device cannot exceed the unicast route limit supported by the device.


Format
------

**routing-table limit** *number* { *alert-percent* | **simply-alert** }

**undo routing-table limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of routes supported by a VPN instance. | The value is an integer ranging from 1 to 4294967295. |
| *alert-percent* | Specifies the percentage of the maximum number of routes. When the maximum number of routes that join the VPN instance is up to the value (number\*alert-percent)/100, the system prompts alarms. The VPN routes can be still added to the routing table, but after the number of routes reaches number, the subsequent routes are dropped. | An integer ranging from 1 to 100. |
| **simply-alert** | Indicates that when VPN routes exceed number, routes can still be added into the routing table, but the system prompts alarms. However, after the total number of VPN routes and network public routes reaches the unicast route limit supported by the device, the subsequent VPN routes are dropped. | - |



Views
-----

VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To prevent excessive routes from being imported into the routing table of the IPv4 or IPv6 address family of a VPN instance, run the routing-table limit command to limit the maximum number of routes in the routing table. If the number of routes in the routing table of the IPv4 or IPv6 address family of a VPN instance exceeds the upper threshold, the excessive routes cannot be advertised to the peer. After the **undo routing-table limit** command is run, the excessive routes will be added to the VPN instance's routing table.



**Precautions**



If simply-alert is configured, only an alarm is reported when the number of routes exceeds the threshold, and route addition is not affected.If the total number of IPv4 routes in a VPN instance exceeds the upper limit, both the L3VPN\_MIB\_TRAP\_THRESH\_EXCEED and hwL3vpnIpv4RouteExceed alarms are reported. If the total number of IPv4 routes in a VPN instance exceeds the middle threshold, both the L3VPN\_MIB\_TRAP\_MID\_THRESH\_EXCEED and hwL3vpnIpv4RouteThresholdExceed alarms are reported.After the **undo routing-table limit** command is run, a large number of routes may be learned, causing route overload or memory overload.




Example
-------

# Set the alarm threshold of the number of routes that the IPv4 address family of the VPN instance named vpn1 can import to 1000.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[~HUAWEI-vpn-instance-vpn1] ipv4-family
[~HUAWEI-vpn-instance-vpn1-af-ipv4] routing-table limit 1000 simply-alert

```