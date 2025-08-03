peer advertise add-path path-number(BGP-IPv4 unicast address family view)
=========================================================================

peer advertise add-path path-number(BGP-IPv4 unicast address family view)

Function
--------



The **peer advertise add-path path-number** command sets the number of preferred routes to be advertised to a specified peer.

The **undo peer advertise add-path** command restores the default configurations.



By default, BGP advertises only one optimal route to its peer.


Format
------

**peer** *peerIpv4Addr* **advertise** **add-path** **path-number** *number* [ **route-policy** *route-policy-name* ]

**undo peer** *peerIpv4Addr* **advertise** **add-path**

**undo peer** *peerIpv4Addr* **advertise** **add-path** **path-number** *number* **route-policy** *route-policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **path-number** *number* | Specifies the maximum number of routes that the device can send to a peer. | The value is an integer ranging from 2 to 64. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


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

To allow a device to accept Add-Path routes received from a specified peer, run the **peer capability-advertise add-path receive** command.A device can advertise Add-Path routes to IBGP/EBGP peers, and Add-Path routes are advertised based on existing route advertisement rules.This command supports only if-match, but not the apply action.Deploying BGP Add-Path may cause traffic loops. Therefore, exercise caution when configuring BGP Add-Path.


Example
-------

# Configure the device to advertise three preferred routes to a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] bestroute add-path path-number 6
[*HUAWEI-bgp] peer 172.16.1.1 as-number 100
[*HUAWEI-bgp] peer 172.16.1.1 capability-advertise add-path send
[*HUAWEI-bgp] peer 172.16.1.1 advertise add-path path-number 3 route-policy test-policy

```