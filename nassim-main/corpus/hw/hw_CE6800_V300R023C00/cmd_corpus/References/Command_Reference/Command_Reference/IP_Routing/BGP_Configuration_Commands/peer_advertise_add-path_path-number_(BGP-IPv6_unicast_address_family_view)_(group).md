peer advertise add-path path-number (BGP-IPv6 unicast address family view) (group)
==================================================================================

peer advertise add-path path-number (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer advertise add-path path-number** command sets the number of preferred routes to be advertised to a specified peer group.

The **undo peer advertise add-path** command restores the default configurations.



By default, the device sends only the optimal route to a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *groupName* **advertise** **add-path** **path-number** *number* [ **route-policy** *route-policy-name* ]

**undo peer** *groupName* **advertise** **add-path**

**undo peer** *groupName* **advertise** **add-path** **path-number** *number* **route-policy** *route-policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupName* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
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

After BGP Add-Path is configured on an RR, the RR needs to send BGP Add-Path routes to a specified peer group. To configure the maximum number of routes that the RR can send to a specified peer group, run the **peer advertise add-path path-number** command. The actual number of preferred routes to be advertised to a peer group is the smaller value between the number of routes configured using the **peer advertise add-path path-number** command and the number of selected routes. If the number of routes to be sent to a peer group is less than the number of optimal routes, BGP selects routes based on BGP route selection rules.

**Prerequisites**

The **peer advertise add-path path-number** command takes effect only if the following conditions are met:

* BGP Add-Path has been enabled and the number of routes that the device can select has been configured using the **bestroute add-path** command.
* The device has been enabled to send Add-Path routes to a specified peer using the **peer capability-advertise add-path send** command.

**Precautions**

To allow a device to accept Add-Path routes received from a specified peer, run the **peer capability-advertise add-path receive** command.A device can advertise Add-Path routes to IBGP/EBGP peers, and Add-Path routes are advertised based on existing route advertisement rules.This command supports only if-match, but not the apply action.Deploying BGP Add-Path may cause traffic loops. Therefore, exercise caution when configuring BGP Add-Path.


Example
-------

# Configure the device to advertise three preferred routes to a peer group.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] bestroute add-path path-number 6
[*HUAWEI-bgp-af-ipv6] peer test capability-advertise add-path send
[*HUAWEI-bgp-af-ipv6] peer test advertise add-path path-number 3 route-policy test-policy

```