peer group (BGP-EVPN address family view) (IPv6)
================================================

peer group (BGP-EVPN address family view) (IPv6)

Function
--------



The **peer group** command adds a peer to a peer group.

The **undo peer group** command removes a peer from a peer group but retains all the configurations of the peer.



By default, a peer is not added to any peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **group** *group-name*

**undo peer** *ipv6-address* **group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The format is X:X:X:X:X:X:X:X. |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale BGP network, there are a large number of peers and many of them have the same routing policies. To configure these peers, you have to repeatedly use some commands. In such a case, configuring peer groups can simplify configurations. If you intend to perform the same configuration on several peers, create and configure a peer group. Then, add the peers to the peer group. The peers will inherit the configurations of the peer group.

**Precautions**

You can add peers of different AS numbers into the same peer group. If a peer has an AS number, the peer keeps its own AS number after being added to a peer group. If a peer has no AS number and a peer group has an AS number, the peer inherits the AS number of the peer group after being added to the peer group.Peers in the same peer group can have different import and export routing policies configured.The **undo peer group** command has the same function as the undo peer and undo peer enable commands.


Example
-------

# Create an IBGP peer group named test, and then add a peer to it.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:db8:1::1 as-number 100
[*HUAWEI-bgp] group test1 internal
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer test1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 group test1

```