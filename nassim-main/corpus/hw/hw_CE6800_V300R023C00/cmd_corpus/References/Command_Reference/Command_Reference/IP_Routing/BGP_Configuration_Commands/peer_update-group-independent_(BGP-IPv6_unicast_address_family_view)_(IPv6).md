peer update-group-independent (BGP-IPv6 unicast address family view) (IPv6)
===========================================================================

peer update-group-independent (BGP-IPv6 unicast address family view) (IPv6)

Function
--------

By default, no peer is set as an independent update peer-group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **update-group-independent** **enable**

**peer** *ipv6-address* **update-group-independent** **disable**

**undo peer** *ipv6-address* **update-group-independent** **enable**

**undo peer** *ipv6-address* **update-group-independent** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve the efficiency of route advertisement, BGP uses the dynamic update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.To address this problem, you can run the **peer update-group-independent** command to set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer. However, if a specified peer or each peer in a peer group is set as an independent update peer-group, the advantages of the dynamic update peer-group mechanism cannot be brought into full play. Therefore, this command is used only when users have such a requirement.

**Prerequisites**

A peer has been added to an update peer-group using the peer group command.

**Precautions**

The configuration of a peer takes precedence over that of the peer group to which the peer belongs. For example, if the **peer update-group-independent disable** command is run for a peer and the **peer update-group-independent** command is run for the peer group to which the peer belongs, the configuration of the peer prevails. That is, the peer is not set as an independent update peer-group.On a device with a large memory, you are advised to run the **peer update-group-independent** command to prevent network resource waste by route sending back.


Example
-------

# Set a specified peer as an independent update peer-group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 update-group-independent enable

```