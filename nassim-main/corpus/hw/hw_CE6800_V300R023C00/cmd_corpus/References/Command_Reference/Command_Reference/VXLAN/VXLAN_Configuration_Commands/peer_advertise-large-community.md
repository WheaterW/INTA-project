peer advertise-large-community
==============================

peer advertise-large-community

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **advertise-large-community** [ **disable** ]

**undo peer** *peerIpv6Addr* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP EVPN peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **disable** | Disables a device from advertising the Large-Community attribute to a peer. | - |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer, run the **peer advertise-large-community** command.

**Prerequisites**

A route-policy has been used to define the large-community attribute.


Example
-------

# Configure a device to advertise the Large-Community attribute to a BGP EVPN IPv6 peer.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix 1 permit 2001:db8::2 96
[*HUAWEI] route-policy RP permit node 10
[*HUAWEI-route-policy] if-match ipv6-prefix 1
[*HUAWEI-route-policy] apply large-community 35551:100:65552 additive
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:db8::2 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:db8::2 enable
[*HUAWEI-bgp-af-evpn] peer 2001:db8::2 advertise-large-community

```