group (BGP-VPN instance IPv6 address family view)
=================================================

group (BGP-VPN instance IPv6 address family view)

Function
--------



The **group** command creates a peer group.

The **undo group** command deletes a peer group.



By default, no peer group is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**group** *group-name* { **external** | **internal** }

**group** *group-name*

**undo group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **external** | Creates an EBGP peer group. | - |
| **internal** | Creates an IBGP peer group. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A peer group consists of peers with the same routing policies. After a peer is added to a peer group, it inherits the configurations of this peer group. When the configurations of the peer group are changed, the configurations of these peers are changed accordingly.On a large-scale BGP network, there are a large number of peers, many of which require the same policy. In such a case, you can run the **group** command to create a peer group, configure the policy for the peer group, and then add peers to the group, which simplifies configurations.

**Configuration Impact**



If the **group** command is run more than once, all configurations take effect.After the **group** command is run, the system creates a BGP peer group of the specified type.



**Precautions**

After a peer group is deleted, all the peers in the peer group are deleted.If no type (IBGP or EBGP) is specified for a peer group, an IBGP peer group is created by default.If an attribute configuration of a BGP peer in a peer group differs from that of the peer group, you can disable the attribute configuration of the peer using an undo command; then the peer inherits the attribute configuration of the peer group.If you run the **undo group** command, all configurations related to the peer group are deleted. Therefore, exercise caution when running this command.Note:Deleting a peer group will disconnect the peers without AS numbers configured in the peer group. Therefore, before deleting a peer group, delete these peers or configure AS numbers for these peers.The functions configured on a peer using the following commands take precedence over those configured on the peer group of the peer:

* peer bfd
* peer bfd block
* peer bfd enable
* peer listen-only
* peer valid-ttl-hopsFor other BGP commands, the latest configuration preferentially takes effect.


Example
-------

# Create an EBGP peer group ex and set its AS number to 500.1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] group ex external
[*HUAWEI-bgp-6-vpna] peer ex as-number 500.1

```

# Create an IBGP peer group named in.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] group in internal

```