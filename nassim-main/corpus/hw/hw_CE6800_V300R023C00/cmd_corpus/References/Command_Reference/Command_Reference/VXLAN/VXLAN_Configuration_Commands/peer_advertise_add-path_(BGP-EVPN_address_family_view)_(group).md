peer advertise add-path (BGP-EVPN address family view) (group)
==============================================================

peer advertise add-path (BGP-EVPN address family view) (group)

Function
--------



The **peer advertise add-path** command configures the maximum number of routes that the device can send to a specified peer.

The **undo peer advertise add-path** command restores the default configurations.



By default, the device sends only the optimal route to a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **advertise** **add-path** **path-number** *path-number*

**undo peer** *group-name* **advertise** **add-path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **path-number** *path-number* | Specifies the maximum number of routes that the device can send. | The value is an integer ranging from 2 to 64. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After BGP Add-Path is configured on an RR, the RR needs to send routes to a specified peer. To configure the maximum number of routes that the RR can send to the peer, run the **peer advertise add-path** command. The actual number of routes that the RR can send to the peer is the smaller one of the value configured using the **peer advertise add-path** command and the actual number of routes selected by the RR. If the maximum number of routes that the RR can send to the peer is less than the actual number of routes selected by the RR, the RR selects the optimal and Add-Path routes based on the BGP route selection rules.

**Prerequisites**

The following operations have been performed:

* BGP Add-Path has been enabled and the maximum number of routes that an RR can select has been configured using the **bestroute add-path** command.
* The RR has been enabled to send Add-Path routes to a specified peer using the **peer capability-advertise add-path send** command.

**Precautions**

* To enable a device to receive Add-Path routes from a specified BGP peer, run the **peer capability-advertise add-path receive** command on the device.
* A device can send Add-Path routes to its BGP peers, and Add-Path routes are advertised based on BGP route advertisement rules.

Example
-------

# Set the maximum number of routes that the device can send to a BGP EVPN peer group to 3.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] peer 2.2.2.2 as-number 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 2.2.2.2 enable
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer 2.2.2.2 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 advertise add-path path-number 3

```