peer group (BGP-IPv4 unicast address family view) (IPv6)
========================================================

peer group (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer group** command adds a peer to a peer group.

The **undo peer group** command removes a peer from a peer group but retains all the configurations of the peer.



By default, no peer group is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **group** *peerGroupName*

**undo peer** *peerIpv6Addr* **group** *peerGroupName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *peerGroupName* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale BGP network, there are a large number of peers and many of them have the same routing policies. To configure these peers, you have to repeatedly use some commands. In such a case, configuring peer groups can simplify configurations. If you intend to perform the same configuration on several peers, create and configure a peer. Then, add the peers to the peer group. The peers will inherit the configurations of the peer group.

**Precautions**

Peers with different AS numbers can be added to the same peer group. If a peer has its own AS number, the peer keeps its own AS number even after being added to a peer group. If a peer has no AS number but the peer group to which the peer will be added has an AS number, the peer inherits the AS number of the peer group after being added to the peer group.Peers in the same peer group can have different import and export routing policies configured.The **undo peer group** command has the same function as the undo peer or **undo peer enable** command.

By default, the peers in a peer group inherit the functions of the peer group. Therefore, if the same peer configuration command is configured for a peer and the peer group to which the peer belongs, the **display this** command may not display the peer configuration command for the peer, and this does not indicate configuration loss. If the peer configuration command supports the disable keyword, the configuration of the peer is also displayed. For example:

* Some parameters in the **peer capability-advertise** command support the disable keyword. If the **peer capability-advertise** command with the disable keyword specified is configured for a peer and its peer group, the **peer capability-advertise** command with this parameter specified is displayed for both the peer and the peer group.
* The **peer allow-as-loop** command does not support the disable keyword. If the **peer allow-as-loop** command is configured for a peer and its peer group, the **peer allow-as-loop** command is displayed only for the peer group, not for the peer.

Example
-------

# Create an IBGP peer group named test and add a peer to the peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv4] peer test enable
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 group test

```