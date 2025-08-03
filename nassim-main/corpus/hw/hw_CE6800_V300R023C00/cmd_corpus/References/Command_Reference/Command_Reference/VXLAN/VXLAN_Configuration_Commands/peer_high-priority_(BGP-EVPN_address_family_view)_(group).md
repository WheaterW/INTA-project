peer high-priority (BGP-EVPN address family view) (group)
=========================================================

peer high-priority (BGP-EVPN address family view) (group)

Function
--------



The **peer high-priority** command enables a device to preferentially select routes based on their priorities in the EVPN address family.

The **undo peer high-priority** command disables a device from preferentially selecting routes based on their priorities in the EVPN address family.



By default, routes are preferentially selected based on BGP route selection rules in the EVPN address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **high-priority**

**undo peer** *peerGroupName* **high-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The EVPN address family supports the coexistence of IPv4 and IPv6 peers. A device may learn routes with the same prefix from IPv4 and IPv6 peers. To control the route priority, run the route-priority command. This function takes effect only locally and is not transmitted through packets.


Example
-------

# Configure a specified peer group to preferentially select a route with a higher priority in the EVPN address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] group g1
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer g1 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.1 group g1
[*HUAWEI-bgp-af-evpn] peer g1 high-priority

```