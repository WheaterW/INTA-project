peer advertise add-path path-number(BGP-IPv6 unicast address family view) (IPv6)
================================================================================

peer advertise add-path path-number(BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer advertise add-path path-number** command sets the number of preferred routes to be advertised to a specified peer.

The **undo peer advertise add-path** command restores the default configurations.



By default, the device sends only the optimal route to a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **advertise** **add-path** **path-number** *number* [ **route-policy** *route-policy-name* ]

**undo peer** *peerIpv6Addr* **advertise** **add-path**

**undo peer** *peerIpv6Addr* **advertise** **add-path** **path-number** *number* **route-policy** *route-policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **path-number** *number* | Specifies the maximum number of routes that the device can send to a peer. | The value is an integer ranging from 2 to 64. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After BGP Add-Path is configured on an RR, the RR needs to send BGP Add-Path routes to a specified BGP peer. To configure the maximum number of routes that the RR can send to a specified BGP peer, run the **peer advertise add-path path-number** command. The actual number of preferred routes advertised to the peer is the smaller value between the number of routes configured using the **peer advertise add-path path-number** command and the number of selected routes. If the number of routes that the RR can send to the peer is less than the actual number of routes selected by the RR, the RR selects routes based on the BGP route selection rules.

**Prerequisites**

The **peer advertise add-path path-number** command takes effect only if the following conditions are met:

* BGP Add-Path has been enabled and the number of routes that the device can select has been configured using the **bestroute add-path** command.
* The device has been enabled to send Add-Path routes to a specified peer using the **peer capability-advertise add-path send** command.

**Precautions**

* The device that receives Add-Path routes can accept the Add-Path routes only after being enabled to accept Add-Path routes from a specified peer using the **peer capability-advertise add-path receive** command.
* A device can advertise Add-Path routes to IBGP/EBGP peers, and Add-Path routes are advertised based on existing route advertisement rules.
* If this command is run on a specified peer and the **peer advertise best-external** command is run in a specified peer group, when the peer is added to the peer group, the peer cannot inherit the function of the **peer advertise best-external** command run on the peer group.
* This command supports only the if-match action, but not the apply action.

Example
-------

# Configure the device to advertise three preferred routes to a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] bestroute add-path path-number 6
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 capability-advertise add-path send
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 advertise add-path path-number 3 route-policy test-policy

```