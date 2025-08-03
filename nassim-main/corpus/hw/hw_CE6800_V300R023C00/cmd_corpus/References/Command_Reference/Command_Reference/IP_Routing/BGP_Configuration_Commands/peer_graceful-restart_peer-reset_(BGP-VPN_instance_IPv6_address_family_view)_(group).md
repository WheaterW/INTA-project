peer graceful-restart peer-reset (BGP-VPN instance IPv6 address family view) (group)
====================================================================================

peer graceful-restart peer-reset (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer graceful-restart peer-reset** command enables the device to reset a BGP connection with a peer group in Graceful Restart (GR) mode.

The **undo peer graceful-restart peer-reset** command restores the default configuration.



By default, a device is not enabled to reset the BGP connection with a specified peer in GR mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **graceful-restart** **peer-reset**

**undo peer** *group-name* **graceful-restart** **peer-reset**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Currently, BGP does not support dynamic capability negotiation. Therefore, BGP capability changes cause peer relationships to be re-established and routing entries to be deleted, interrupting services. To solve this problem, you can run the **peer graceful-restart peer-reset** command to reset the BGP connection with a specified peer group in GR mode after enabling GR on the BGP peer.After the function of resetting the BGP connection with a specified peer group in GR mode is configured, if the BGP peer relationship of another address family is established based on the BGP IPv4 unicast peer session, BGP starts to reset the BGP connection with the specified peer group in GR mode and renegotiates the capability. During this process, the BGP IPv4 unicast peer session is re-established, but the original routing entries are not deleted. The forwarding module can still forward packets based on the routing information, ensuring uninterrupted IPv4 services.

**Prerequisites**

GR has been enabled for a peer group using the **peer capability-advertise graceful-restart** command. After GR is enabled for a peer group for the first time, all sessions and instances are deleted and re-established, causing service interruptions.

**Precautions**

If the **peer capability-advertise graceful-restart** command is run but the **peer graceful-restart peer-reset** command is not run, the peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation will not reset the BGP connection in GR mode. The peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation resets the BGP connection in GR mode only after both the peer capability-advertise graceful-restart and **peer graceful-restart peer-reset** commands are run.


Example
-------

# Enable a device to use the GR mode to reset BGP connections with all peers in a specified group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] group aaa
[*HUAWEI-bgp-6-vpna] peer aaa capability-advertise graceful-restart
[*HUAWEI-bgp-6-vpna] peer aaa graceful-restart peer-reset

```