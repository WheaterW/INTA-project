peer advertise add-path (bgp-muli-instance-af-evpn view)
========================================================

peer advertise add-path (bgp-muli-instance-af-evpn view)

Function
--------



The **peer advertise add-path** command configures the maximum number of routes that the device can send to a specified peer.

The **undo peer advertise add-path** command restores the default configurations.



By default, the device sends only the optimal route to a BGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **advertise** **add-path** **path-number** *number*

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **advertise** **add-path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **path-number** *number* | Specifies the maximum number of routes that the device can send. | The value is an integer ranging from 2 to 64. |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After BGP Add-Path is configured on an RR, the RR needs to send routes to a specified BGP peer. To configure the maximum number of routes that the RR can send to the peer, run the **peer advertise add-path** command. The actual number of routes that the RR can send to the peer is the smaller one of the value configured using the **peer advertise add-path** command and the actual number of routes selected by the RR. If the maximum number of routes that the RR can send to the peer is less than the actual number of routes selected by the RR, the RR selects the optimal and Add-Path routes based on the BGP route selection rules.

**Prerequisites**

The following operations have been performed:

* BGP Add-Path has been enabled and the maximum number of routes that an RR can select has been configured using the **bestroute add-path** command.
* The RR has been enabled to send Add-Path routes to a specified IBGP peer using the **peer capability-advertise add-path send** command.

**Precautions**

* To enable a device to receive Add-Path routes from a specified BGP peer, run the **peer capability-advertise add-path receive** command on the device.
* A device advertises Add-Path routes to its BGP peers based on BGP route advertisement rules.

Example
-------

# Set the maximum number of Add-Path routes that the device can send to a peer in the BGP multi-instance EVPN address family view.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] l2vpn-family evpn
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 advertise add-path path-number 3

```