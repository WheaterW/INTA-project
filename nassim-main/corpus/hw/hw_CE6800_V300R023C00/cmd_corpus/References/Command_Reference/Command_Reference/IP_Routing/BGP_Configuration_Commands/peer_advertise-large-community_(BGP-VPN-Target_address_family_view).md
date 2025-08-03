peer advertise-large-community (BGP-VPN-Target address family view)
===================================================================

peer advertise-large-community (BGP-VPN-Target address family view)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **advertise-large-community** [ **disable** ]

**undo peer** { *ipv4-address* | *ipv6-address* } **advertise-large-community** [ **disable** ]

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **advertise-large-community** [ **disable** ]

**undo peer** *ipv4-address* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer or peer group, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer group, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**

Specific Large-Community values have been defined in a route-policy.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 advertise-large-community

```