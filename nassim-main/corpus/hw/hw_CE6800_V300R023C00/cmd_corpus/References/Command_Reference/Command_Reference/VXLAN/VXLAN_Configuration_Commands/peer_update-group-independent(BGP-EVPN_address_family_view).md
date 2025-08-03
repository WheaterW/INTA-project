peer update-group-independent(BGP-EVPN address family view)
===========================================================

peer update-group-independent(BGP-EVPN address family view)

Function
--------



The **peer update-group-independent enable** command sets a specified peer or each peer in a peer group as an independent update peer-group.

The **peer update-group-independent disable** command removes the setting of a specified peer or each peer in a peer group as an independent update peer-group.

The **undo peer update-group-independent enable** command removes the setting of a specified peer or each peer in a peer group as an independent update peer-group.

The **undo peer update-group-independent disable** command sets a specified peer or each peer in a peer group as an independent update peer-group.



By default, no peer is set as an independent update peer-group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **update-group-independent** **enable**

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **update-group-independent** **disable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **update-group-independent** **enable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **update-group-independent** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The format is X:X:X:X:X:X:X:X. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve the efficiency of route advertisement, BGP uses the dynamic update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.To address this problem, you can run the **peer update-group-independent** command to set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer. However, if a specified peer or each peer in a peer group is set as an independent update peer-group, the advantages of the dynamic update peer-group mechanism cannot be brought into full play. Therefore, this command is used only when users have such a requirement.

**Precautions**

The configuration of the peer level takes precedence over that of the peer group level. For example, if the peer { ipv4-address | ipv6-address } update-group-independent disable command is run for a peer and the peer group-name update-group-independent command is run for the peer group to which the peer belongs, the configuration for the peer takes effect. Specifically, the peer is disabled from being an independent update peer-group.On a device with large memory, you are advised to run the **peer update-group-independent** command to prevent routes from being sent back, thereby saving network resources.


Example
-------

# Set a specified peer as an independent update peer-group.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.1 update-group-independent enable

```